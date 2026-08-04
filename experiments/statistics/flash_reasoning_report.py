#!/usr/bin/env python3
"""Generate a reasoning-process audit for DeepSeek V4 Flash."""

from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def pct(n: int, d: int) -> str:
    return f"{100*n/d:.2f}%" if d else "—"


def category(record: dict) -> str:
    if record.get("prediction") is None:
        return "invalid"
    if record.get("prediction") == "unknown":
        return "unknown"
    if not record.get("verdict_correct"):
        return "wrong_verdict"
    if record.get("expected") == "unsat":
        return "correct_unsat"
    if record.get("sat_witness_valid"):
        return "valid_sat"
    return "sat_not_verified"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch", nargs="?", default="v2")
    args = parser.parse_args()
    batch_set = read_json(ROOT / "experiments" / "benchmark-sets" / f"{args.batch}.json")
    excluded = {item["case"] for item in batch_set["excluded_cases"]}
    runs_root = ROOT / "experiments" / "deepseek-v4-flash" / "runs"
    run_dir = sorted(p for p in runs_root.iterdir() if p.is_dir())[-1]
    records = [json.loads(line) for line in (run_dir / "results" / "runs.jsonl").read_text(encoding="utf-8").splitlines()]
    records = [record for record in records if record["case"] not in excluded]
    records.sort(key=lambda r: (r["case"], r["run"]))
    if len(records) != batch_set["planned_slots_per_model"]:
        raise RuntimeError(f"expected {batch_set['planned_slots_per_model']} records, found {len(records)}")

    counts = Counter(category(record) for record in records)
    verification = Counter(
        (record.get("verification") or {}).get("verification_result")
        for record in records
        if category(record) == "sat_not_verified"
    )
    reasoning_paths = []
    for record in records:
        path = run_dir / "raw" / Path(record["case"]).with_suffix("") / f"run-{record['run']:02d}.reasoning.txt"
        if path.exists():
            reasoning_paths.append(path)

    token_by_category = defaultdict(list)
    latency_by_category = defaultdict(list)
    for record in records:
        label = category(record)
        token_by_category[label].append(
            record.get("usage", {}).get("completion_tokens_details", {}).get("reasoning_tokens", 0)
        )
        latency_by_category[label].append(record.get("latency_seconds", 0))

    wrong_direction = Counter(
        (record["expected"], record["prediction"])
        for record in records if category(record) == "wrong_verdict"
    )
    invalid_length = sum(
        category(record) == "invalid" and record.get("finish_reason") == "length"
        for record in records
    )

    by_logic = defaultdict(Counter)
    for record in records:
        by_logic[record["logic"]][category(record)] += 1

    lines = []
    add = lines.append
    add(f"# {args.batch} DeepSeek V4 Flash reasoning 过程分析")
    add("")
    add("> 本报告分析正式 93 题集合中的 465 次独立运行。分析材料包括保存的 `reasoning.txt`、最终 JSON、逐次评分字段和 cvc5 验证结果。reasoning 是模型 API 实际返回并由运行器保存的 thinking 内容。结论只适用于本批样本和当前提示/配置。")

    add("")
    add("## 1. 数据覆盖与结果分解")
    add("")
    add(f"- 纳入评分记录：{len(records)}；reasoning 文件：{len(reasoning_paths)}。")
    add(f"- 正确 UNSAT：{counts['correct_unsat']}；正确且 witness 有效的 SAT：{counts['valid_sat']}。")
    add(f"- Verdict 错误：{counts['wrong_verdict']}；正确 SAT 但未验证成功：{counts['sat_not_verified']}；不可解析响应：{counts['invalid']}。")
    add("")
    add("| 结果类别 | 次数 | 占 465 次比例 | reasoning tokens 中位数 | 平均耗时（秒） |")
    add("|---|---:|---:|---:|---:|")
    labels = [
        ("correct_unsat", "正确 UNSAT"), ("valid_sat", "正确 SAT + 有效 witness"),
        ("wrong_verdict", "Verdict 错误"), ("sat_not_verified", "正确 SAT、witness 未验证成功"),
        ("invalid", "最终响应 invalid"),
    ]
    for key, label in labels:
        toks = token_by_category[key]
        times = latency_by_category[key]
        add(f"| {label} | {counts[key]} | {pct(counts[key], len(records))} | {statistics.median(toks):.0f} | {statistics.mean(times):.1f} |")

    add("")
    add("最明显的过程信号是：正确 UNSAT 的 reasoning 中位数最短；错误 verdict 和未验证 SAT 明显更长；31 次 invalid 中全部因 `finish_reason=length` 用尽输出长度，其中大部分 reasoning 达到 32768 tokens。这反映的不是‘想得越久越正确’，而是困难题上反复探索、回溯和格式犹豫却未收敛。")

    add("")
    add("### Verdict 错误方向")
    add("")
    add("| Golden → 预测 | 次数 | 含义 |")
    add("|---|---:|---|")
    add(f"| SAT → UNSAT | {wrong_direction[('sat', 'unsat')]} | 构造解失败或错误推出矛盾 |")
    add(f"| UNSAT → SAT | {wrong_direction[('unsat', 'sat')]} | 候选赋值只满足局部条件，漏掉矛盾 |")

    add("")
    add("## 2. Reasoning 做得好的地方")
    add("")
    add("### 2.1 能恢复 Tseitin 外壳的结构")
    add("")
    add("成功 reasoning 经常先给理论原子命名，再把三类 clause 识别为 `τ ↔ A∧B`、`τ ↔ A∨B`，并从单位 clause 正向传播。这个做法把长 CNF 压缩成依赖图，减少逐字符处理，是 Flash 最有效的推理策略。")
    add("")
    add("### 2.2 会构造具体候选模型并逐项检查")
    add("")
    add("在成功的 ABVFP 和部分数组题中，reasoning 会先选择全零数组、`+zero` 浮点值或简单整数，再回到强制等式逐项检查。它也会注意必须覆盖每个原始声明，并区分零元常量与正元函数。该流程与验证器需要的证书结构基本一致。")
    add("")
    add("### 2.3 能识别高层数学结构")
    add("")
    add("在 `NRA/722eaea277-strassen-hard.md` 中，模型正确识别出公式表达 2×2 矩阵乘法的 rank-7 分解，并联系到 Strassen 构造，因此五次 verdict 都正确为 SAT。这说明模型对公式语义的抽象识别可以超越外层只有一个 clause 的表面表示。")
    add("")
    add("### 2.4 会进行输出协议自检")
    add("")
    add("不少 reasoning 末尾会检查：是否只输出 JSON、是否包含全部声明、是否错误加入 `τ` 辅助变量、函数参数字段和 SMT-LIB term 是否合规。成功运行中这种‘推理后再做证书审计’很有价值。")

    add("")
    add("## 3. Reasoning 哪里做错了，以及怎么错")
    add("")
    add("这一节把失败分成五类。前两类主要是模型逻辑或证书理解错误；第三、第四类中有一部分只是验证器没有在时限内确认，不能直接说模型数学上错了；第五类是模型没有及时结束推理。")
    add("")
    add("### 3.1 Tseitin 链过长时，混淆等价方向或分支作用域")
    add("")
    add("**先看一个最小例子。** 假设 `τ ↔ (A ∨ B)`，且 `τ=true`。正确结论只是 `A`、`B` 至少一个为真；不能同时推出 `A=true` 和 `B=true`。如果 `A` 表示 `x=0`、`B` 表示 `x=1`，把 OR 错当 AND 就会制造出 `x=0 ∧ x=1` 的假矛盾。")
    add("")
    add("另一个方向错误是：由 `τ ↔ (A ∧ B)` 可以得到 `τ→A`，但不能只由 `A` 反推 `τ`；还必须知道 `B`。长链中只要把一次单向蕴含倒过来，后面即使每一步都正确，也是在错误前提上继续推理。")
    add("")
    add("**Flash 的真实表现。** 在 `QF_ALIA/b1092fb93e-qlock.base.30.md` 中，reasoning 沿 `τ1362 → … → τ1237` 追踪上千个辅助变量，认为一组条件强制 `x14∈{0,1,2}`，另一组条件强制 `x14=3`，于是宣布 UNSAT。但 golden 是 SAT，说明这个‘同时强制’关系并不存在。由于推导跨越大量节点，仅从自然语言日志不能严谨锁定唯一错句；可以确定的是，它在某处错误恢复了 AND/OR、蕴含方向或分支作用域。该题五次中三次输出错误 UNSAT、两次耗尽长度，属于稳定困难。")
    add("")
    add("**正确做法。** 对每个辅助变量单独记录 `类型=AND/OR`、`正向可推出什么`、`反向需要哪些条件`。遇到 OR 必须保留所有尚未排除的分支；发现一个分支矛盾，只能关闭该分支，不能直接判整个公式 UNSAT。")
    add("")
    add("**对应测试用例。** 下表中的 qlock 用例都表现出长 Tseitin 链困难；只有第一题已通过逐段阅读定位到上述具体错误形态，其余题依据错误 verdict、长度耗尽和相似 reasoning 归为同一风险族，不声称每题都在完全相同的 clause 上出错。")
    add("")
    add("| Logic | 测试用例 | 5 次中的表现 | 简短分析 |")
    add("|---|---|---|---|")
    add("| QF_ALIA | `b1092fb93e-qlock.base.30.md` | 3 次假 UNSAT，2 次长度耗尽 | reasoning 构造出 `x14∈{0,1,2}` 与 `x14=3` 的假冲突，是最明确的长链恢复错误 |")
    add("| QF_ALIA | `28114b6375-qlock-bug2-10.md` | 3 次假 UNSAT，2 次长度耗尽 | 多分支状态链无法稳定收敛；错误方向与上一题相同，但未定位到唯一错句 |")
    add("| QF_ALIA | `96eb0f0ccb-qlock.base.20.md` | 4 次假 UNSAT，1 次长度耗尽 | 对 SAT 公式反复推出矛盾，说明长链分支被过度约束 |")
    add("| QF_ALIA | `60d1a1277d-qlock.induction.25.md` | 5 次全部长度耗尽 | 甚至没有形成 verdict，属于链条规模导致的完全不收敛 |")
    add("| QF_ALIA | `d6617f16d8-qlock.induction.16.md` | 5 次全部长度耗尽 | reasoning 持续追踪状态分支，却未压缩成可管理的依赖图 |")
    add("| QF_ALIA | `76fabb1637-stack-invalid-6.md` | 2 次假 UNSAT，其余 3 次成功 | 不是稳定失败，说明模型偶尔能正确保留分支，但重复运行存在波动 |")

    add("")
    add("### 3.2 找到 SAT 思路，但 witness 没有真正封闭")
    add("")
    add("**先看一个最小例子。** 输入声明只有 `x:Int`，CNF 转换另外引入 `τ1`。SAT 证书应该只给原始声明赋值，例如 `x=3`；`τ1` 是内部辅助符号，可由 CNF 约束扩展。若证书额外提交 `τ1=true`，验证器会发现证书符号集合与原始声明不一致。反过来，如果漏掉 `x`，证书也不完整。")
    add("")
    add("**Flash 的真实表现。** 在 LIA Frobenius 类题中，它能分析 `197x+199y` 一类表示问题，推出候选最大不可表示数，并正确回答 SAT。可是 reasoning 末尾反复讨论‘要不要把 `τ1` 也加入 constants’。实际运行中出现过 `constant coverage mismatch: extra=['τ1']`。这不是 SAT/UNSAT 数学结论错，而是把内部辅助变量误当成原始证书变量。")
    add("")
    add("另一个‘没有封闭’的例子是只给出看似合理的局部赋值，却没有回代所有 clause。例如模型令所有浮点值为 `+zero`，可能满足多数等式；如果还有一个 clause 要求某个结果非零，那么全零模型仍会被 cvc5 返回 UNSAT。正确 SAT 证书必须覆盖全部原始自由符号，并把候选值回代到全部约束，而不是只检查产生候选值的局部片段。")
    add("")
    add("**正确做法。** 将过程明确拆成两步：第一步只解决数学问题；第二步根据 `declarations` 建立严格清单，逐项检查 symbol、sort、函数参数、SMT-LIB 值和覆盖范围，禁止额外加入 `τ/λ`。")
    add("")
    add("**对应测试用例。**")
    add("")
    add("| Logic | 测试用例 | 具体错误 | 简短分析 |")
    add("|---|---|---|---|")
    add("| LIA | `01b211cc37-fcp_167_173_179.md` | 1 次额外提交 `τ1`；另 4 次验证 timeout | 数学 verdict 五次都正确为 SAT，但证书边界不稳定，且量词公式仍给验证器留下较大工作量 |")
    add("| LIA | `0afccb8013-009.md` | 1 次额外提交 `τ1` | 把内部 Tseitin 变量当成原始声明，触发 coverage mismatch |")
    add("| ABVFP | `dd5e3b0351-float_req_bl_1210_false-unreach-call.c_0.md` | 1 次额外提交 `τ1` | 推理得出 SAT 后，证书清单没有严格以 declarations 为准 |")
    add("| ABVFP | `189893bdbb-float_req_bl_0530b_true-unreach-call.c_2.md` | 1 次括号未闭合，1 次 witness 被 cvc5 反驳 | 一次是 SMT-LIB 表达错误；另一次是具体赋值确实不能满足全部公式 |")
    add("| LIA | `07d23f440c-076.md` | 2 次 witness 被 cvc5 返回 UNSAT | verdict 是 SAT，但候选整数赋值只满足了局部推导，没有封闭全部约束 |")
    add("| NIA | `6097397d24-Problem17_label54_false-unreach-call.c_10.md` | 1 次 witness 被 cvc5 返回 UNSAT | 非线性候选值未能同时满足所有多项式约束 |")
    add("| QF_S | `fae5a3418c-instance12239.md` | 1 次 constant 字段结构错误 | 把声明结构字段直接抄进 certificate，没有转换成要求的 `symbol/sort/value_smt2` |")

    add("")
    add("### 3.3 高层定理识别正确，但没有给验证器可快速确认的证书")
    add("")
    add("这一类问题的关键是区分：**公式外部声明的自由变量**，以及 **`exists` 内部的局部变量**。当前证书只能给前一种变量赋值。")
    add("")
    add("**情况一：`x` 是公式外部声明的自由变量。**")
    add("")
    add("```smt2")
    add("(declare-const x Real)")
    add("(assert (= (* x x) 4))")
    add("```")
    add("")
    add("这里 `x` 出现在输入的 `declarations` 中。模型可以提交 `x=2`，验证器把它加入公式：")
    add("")
    add("```smt2")
    add("(assert (= x 2))")
    add("```")
    add("")
    add("此时 cvc5 只需检查 `2×2=4`，不需要自己寻找 `x`。这才是能够直接执行的具体 witness。")
    add("")
    add("**情况二：`x` 是存在量词内部的局部变量。**")
    add("")
    add("```smt2")
    add("(assert (exists ((x Real)) (= (* x x) 4)))")
    add("```")
    add("")
    add("这里没有 `(declare-const x Real)`。`x` 只在 `exists (...)` 内部有效，离开量词后这个名字就不存在。因此 certificate input 的 `declarations` 是空的；按照当前协议，模型只能提交 `constants:[]`。验证器不能在公式外面直接添加 `(assert (= x 2))`，因为外层没有名为 `x` 的声明。")
    add("")
    add("空 certificate 并不是在说‘没有解’，而是在说‘没有可赋值的自由声明’。原公式仍然可能是 SAT；只是验证器没有收到 `x=2`，所以仍需自己求解 `∃x.x²=4`。简单例子很快，但复杂量词和非线性公式可能 timeout。")
    add("")
    add("**Flash 的真实表现。** `NRA/722eaea277-strassen-hard.md` 大致询问：是否存在一组系数，使 2×2 矩阵乘法对所有输入矩阵都能由 7 次乘法表达。结构可概括为：")
    add("")
    add("```text")
    add("存在 Strassen 系数，使得：对所有矩阵 A、B，七项分解恒等于 A×B")
    add("```")
    add("")
    add("Flash 识别出这就是 Strassen 的 rank-7 分解，因此五次都判断 SAT。这个高层判断有明确数学依据。但是，那些‘待寻找的系数’全部绑定在 `exists` 内部，不在自由 `declarations` 中；模型按当前协议只能输出空 certificate。")
    add("")
    add("于是 cvc5 收到的仍然是完整难题：它既要寻找几十个系数，又要证明这些系数对所有矩阵输入都成立。五次验证都 timeout，而不是返回 UNSAT。因此不能据此说 Flash 的数学结论错误；准确结论是：**SAT 判断正确，但当前证书没有把模型想到的 Strassen 系数传递给验证器。**")
    add("")
    add("要真正验证这种题，证书协议需要增加 `existential_witness`：允许模型给 `exists` 绑定变量提供具体值。验证器先用这些值替换存在变量，再检查剩余公式。对于 `∃x.x²=4`，就是把它变成 `2²=4`；对于 Strassen，就是填入具体系数后只检查矩阵恒等式，而不再让 cvc5 从头寻找系数。")
    add("")
    add("**对应测试用例。**")
    add("")
    add("| Logic | 测试用例 | 5 次中的表现 | 简短分析 |")
    add("|---|---|---|---|")
    add("| NRA | `722eaea277-strassen-hard.md` | 5 次 verdict 均正确为 SAT，5 次验证均 timeout | reasoning 正确识别 Strassen rank-7；自由 declarations 为空，空证书没有携带存在量词中的具体系数 |")
    add("")
    add("本批中只有这一题有足够明确的 reasoning 证据归入‘高层定理识别正确但存在见证无法表达’。其他 timeout 不自动归入此类，因为超时也可能由公式规模或验证器策略造成。")

    add("")
    add("### 3.4 数组 witness 的局部构造合理，但验证结果可能 unknown")
    add("")
    add("**先看一个最小例子。** 若 `a1 = store(a0, 1, 10)`，要证明 `select(a1,1)=10` 很直接；但要给整个数组 `a1` 一个模型，不能只写‘索引 1 是 10’，还要说明其他索引继承 `a0`。若另有函数 `sk(a,b):Int`，证书还必须给出对所有数组参数都定义的函数体，而不只是当前一次调用的返回值。")
    add("")
    add("**Flash 的真实表现。** 在 `QF_AUFLIA/41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md` 中，它选择常量数组作为底层数组，逐次展开 `store`，让两个数组在索引 10 处取不同值，并给 Skolem 函数设计 `ite` 函数体。思路上是在构造数组差异 witness，但五次 cvc5 都返回 `unknown`，所以只能说未验证成功，不能认定模型一定错。")
    add("")
    add("另一个数组题 `QF_AUFLIA/088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md` 出现过明确协议错误：函数参数对象使用了 `name`，协议要求的是 `symbol`；也出现过 cvc5 返回 UNSAT，说明至少一次具体 witness 确实不满足公式。这两类失败必须分开：前者是 JSON/schema 错，后者才是模型值错。")
    add("")
    add("**正确做法。** 数组模型需要同时检查默认值、每次 store 的覆盖顺序、所有被 select 的索引和数组等式；函数必须是对整个参数域都有定义的 total function。生成 JSON 前再做字段级审计，避免 `name/symbol`、括号和 sort 错误。")
    add("")
    add("**对应测试用例。**")
    add("")
    add("| Logic | 测试用例 | 5 次中的表现 | 简短分析 |")
    add("|---|---|---|---|")
    add("| QF_AUFLIA | `41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md` | 5 次正确 SAT，5 次 cvc5 unknown | 数组差异 witness 的构造思路完整，但验证器不能确认；不能判定模型值一定错误 |")
    add("| QF_AUFLIA | `3d0fe3ca5c-swap_invalid_t3_pp_sf_ai_00006_004.cvc.md` | 5 次正确 SAT，5 次 cvc5 unknown | 手工展开 store/swap 后仍留下复杂数组与函数一致性检查 |")
    add("| QF_AUFLIA | `e387ddf96f-storecomm_invalid_t1_pp_sf_ai_00020_001.cvc.md` | 4 次 unknown，1 次函数参数 schema 错 | reasoning 能找到 SAT 构造方向，但机器表达和可判定性都不稳定 |")
    add("| QF_AUFLIA | `088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md` | 1 次 unknown，1 次 schema 错，1 次 witness 被反驳；另 2 次 verdict 错 | 大型数组题同时暴露 verdict、证书格式和具体模型三层问题 |")

    add("")
    add("### 3.5 推理不收敛导致没有最终答案")
    add("")
    add("**最小例子。** 模型先猜 SAT，分析几页后改成 UNSAT，又因为发现另一个分支改回 SAT；如果一直重复而没有在输出上限前提交 JSON，那么评分程序得到的不是一个较差答案，而是根本没有可解析答案。")
    add("")
    add(f"**Flash 的真实表现。** 共有 {counts['invalid']} 次 invalid，且 {invalid_length}/{counts['invalid']} 次都以 `finish_reason=length` 结束。QF_ALIA 占 15 次，QF_AUFLIA 占 6 次。它们的 reasoning 中位数达到 32768 tokens，常见过程是重复解析同一 Tseitin 区段、质疑前一个推论、重新选择分支，并在最后没有留下 JSON 输出空间。")
    add("")
    add("这类失败反映的是推理控制问题：模型没有设置中间结论、剩余预算和停止条件。正确策略应优先保留最终 JSON 的输出空间；当无法可靠完成时，在协议允许的情况下及时返回 `unknown`，会比没有响应更可解释。不过本项目对有 golden SAT/UNSAT 的题仍会把 `unknown` 计为分类错误。")
    add("")
    add("**对应测试用例。** 以下列出出现过 `finish_reason=length` 的全部 13 个正式用例。")
    add("")
    add("| Logic | 测试用例 | 长度耗尽次数/5 | 简短分析 |")
    add("|---|---|---:|---|")
    add("| QF_ALIA | `60d1a1277d-qlock.induction.25.md` | 5 | 长状态链五次均未收敛，是最稳定的输出预算失败之一 |")
    add("| QF_ALIA | `d6617f16d8-qlock.induction.16.md` | 5 | 反复解析 induction 分支，未保留最终 JSON 空间 |")
    add("| NIA | `d2baf9a6e3-184.md` | 4 | 非线性整数关系导致长时间尝试候选值和反证 |")
    add("| QF_AUFLIA | `a6831a3fb1-pp-TakenBranch-s2e.md` | 4 | 数组、函数和路径条件组合使 reasoning 展开失控 |")
    add("| LIA | `4935b59fa2-137.md` | 2 | 大型整数约束中没有及时形成稳定结论 |")
    add("| LIA | `ee94632839-138.md` | 2 | 长算术分析耗尽输出，另外运行仍可给出 verdict |")
    add("| QF_ALIA | `28114b6375-qlock-bug2-10.md` | 2 | 与错误 UNSAT 同时出现，表明分支追踪既可能错判也可能不收敛 |")
    add("| QF_ALIA | `b1092fb93e-qlock.base.30.md` | 2 | 另三次形成假矛盾；是典型长 Tseitin 链困难 |")
    add("| NIA | `520443d627-183.md` | 1 | 偶发耗尽，其他四次说明该题并非稳定不可处理 |")
    add("| QF_ALIA | `96eb0f0ccb-qlock.base.20.md` | 1 | 其余四次均假 UNSAT，主要问题仍是错误链推理 |")
    add("| QF_AUFLIA | `4f8b0ac98d-swap_t1_pp_nf_ai_00006_004.cvc.md` | 1 | 数组 swap reasoning 偶发不收敛 |")
    add("| QF_AUFLIA | `a4c8726cf4-swap_t3_pp_sf_ai_00010_001.cvc.md` | 1 | 大型数组模型生成偶发超过输出预算 |")
    add("| QF_S | `1ac968b76c-benchmark_0286.md` | 1 | 字符串 witness 构造偶发耗尽；同时另有一次 `invalid_output` |")

    add("")
    add("## 4. 正确 SAT 但 witness 未验证成功：必须细分")
    add("")
    add("| 验证结果 | 次数 | 能否认定模型 witness 错误 | 解释 |")
    add("|---|---:|---|---|")
    add(f"| `unsat` | {verification['unsat']} | 可以 | 候选模型与原公式合取后不可满足，是真正的 witness 错误 |")
    add(f"| `timeout` | {verification['timeout']} | 不可以 | 在验证时限内没有结论，只能记为未验证成功 |")
    add(f"| `unknown` | {verification['unknown']} | 不可以 | cvc5 无法确认，可能涉及量词、数组或理论组合 |")
    add(f"| `verifier_error` | {verification['verifier_error']} | 多数是协议错误 | 包括额外 `τ1`、括号未闭合、函数参数键名错误等 |")
    add(f"| `invalid_output` | {verification['invalid_output']} | 是输出失败 | verifier 没得到有效的可检查结果 |")
    add(f"| `invalid_verifier_output` | {verification['invalid_verifier_output']} | 暂不能归因 | 验证器异常输出，需要单独复核 |")
    add("")
    add("因此，50 次未计入有效 SAT witness 不能全部描述成‘模型推理错’：7 次已证明模型值不满足，29 次验证不完备（timeout/unknown），13 次属于模型协议/输出问题，1 次是验证器异常。按照当前指标它们都不进入 SAT 真解率分子，但做能力诊断时必须分开。")

    add("")
    add("## 5. 不同 Logic 在 reasoning 层面的表现")
    add("")
    add("| Logic | 正确UNSAT | 有效SAT | Verdict错 | SAT未验证 | Invalid | Reasoning 特征 |")
    add("|---|---:|---:|---:|---:|---:|---|")
    notes = {
        "ABVFP": "常能用零值构造；难点转为浮点/数组 term 的精确编码",
        "ALIA": "UNSAT 传播较有效；量词和数组关系会造成少量假 SAT",
        "LIA": "数学洞察较强；量词见证与辅助符号边界造成验证困难",
        "NIA": "多数题能抓住代数矛盾或简单赋值，整体稳定",
        "NRA": "能识别结构；量化非线性 closed formula 容易验证超时",
        "QF_ALIA": "最明显的长 Tseitin 链追踪和不收敛问题",
        "QF_AUFLIA": "verdict 尚可，数组/函数完整模型与验证 unknown 是瓶颈",
        "QF_NIRA": "仅一题且为正确 UNSAT，样本不足",
        "QF_S": "整体稳定；少数长字符串值或结构输出失败",
    }
    for logic in sorted(by_logic):
        c = by_logic[logic]
        add(f"| {logic} | {c['correct_unsat']} | {c['valid_sat']} | {c['wrong_verdict']} | {c['sat_not_verified']} | {c['invalid']} | {notes[logic]} |")

    add("")
    add("## 6. 从复杂度特点映射到 reasoning 行为")
    add("")
    add("| 难度类别 | 输入层面的高风险特征 | Reasoning 中的可观察表现 | 常见结果 |")
    add("|---|---|---|---|")
    add("| 总体约束规模 | clause/文本很长 | 重复摘要、忘记前部约束、多次从头解析 | 长度耗尽、漏约束、错误 verdict |")
    add("| 分支复杂度 | literal 多、OR 分支宽且耦合 | 选定一个局部分支后未验证其他 clause；混淆 OR 的存在选择与全局强制 | 假 SAT 或假 UNSAT |")
    add("| 语义复杂度 | 量词、数组、非线性、浮点/位向量 | 使用高层类比代替完整语义检查；量词只用少数实例；浮点按普通实数处理的风险 | verdict 可能正确但论证不充分，或产生错误值 |")
    add("| 证书复杂度 | 声明/函数/数组多、值类型复杂 | 数学结论完成后长时间手写 JSON/SMT term；反复犹豫是否包含辅助变量 | coverage、schema、括号错误，或 witness 未覆盖全局关系 |")

    add("")
    add("## 7. 总结：Flash 的能力画像")
    add("")
    add("Flash 擅长的是把中小规模 CNF 的 Tseitin 外壳还原为逻辑结构、从单位子句传播、发现明显矛盾，以及为简单算术/数组/浮点题构造规则化模型。它在 reasoning 中经常能给出有价值的数学解释，不只是猜测标签。")
    add("")
    add("它最困难的不是单一的‘公式长’，而是长 Tseitin 链、宽分支、理论组合和大 witness 同时出现。此时 reasoning 会表现为过度展开、反复回溯、局部推论被误当成全局结论，以及数学解和证书协议之间切换失败。32768-token invalid 是这种不收敛的最直接证据。")
    add("")
    add("后续报告应新增失败原因字段：`wrong_verdict`、`model_refuted_by_cvc5`、`verification_timeout`、`verification_unknown`、`certificate_schema_error`、`response_length_exhausted`。这样才能区分逻辑能力、证书表达能力和验证基础设施限制。")

    output = ROOT / "experiments" / "statistics" / args.batch / "analyze" / "deepseek_flash_reasoning_report.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
