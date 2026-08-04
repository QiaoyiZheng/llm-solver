#!/usr/bin/env python3
"""Generate a multi-dimensional model-capability report from one statistics batch."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def percent(n: int, d: int) -> str:
    return f"{100 * n / d:.2f}%" if d else "—"


def quantile(values: list[int], q: float) -> int:
    ordered = sorted(values)
    index = min(len(ordered) - 1, math.ceil(q * len(ordered)) - 1)
    return ordered[max(0, index)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch", nargs="?", default="v2")
    args = parser.parse_args()
    stats = ROOT / "experiments" / "statistics" / args.batch
    output = stats / "analyze" / "model_capability_report.md"
    output.parent.mkdir(parents=True, exist_ok=True)

    with (stats / "cases.csv").open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    source_manifest = read_json(ROOT / "benchmarks" / "smtlib-2025" / "manifest.json")
    source = {x["path"].removesuffix(".smt2") + ".md": x for x in source_manifest["benchmarks"]}

    features = {}
    case_paths = {}
    for row in rows:
        benchmark = row["benchmark"]
        case_paths[benchmark] = row["case"]
        if benchmark in features:
            continue
        text = (ROOT / "benchmarks" / "CNF-Bench" / benchmark).read_text(encoding="utf-8")
        clauses = [line for line in text.splitlines() if line.strip()]
        case = read_json(ROOT / "benchmarks" / "certificate-inputs" / "cases" / row["case"])
        declarations = case.get("declarations", [])
        features[benchmark] = {
            "logic": row["logic"],
            "status": source[benchmark]["status"],
            "clauses": len(clauses),
            "literals": sum(line.count("∨") + 1 for line in clauses),
            "max_clause_literals": max((line.count("∨") + 1 for line in clauses), default=0),
            "chars": len(text),
            "source_bytes": source[benchmark]["size"],
            "declarations": len(declarations),
            "functions": sum(bool(d.get("parameter_sorts")) for d in declarations),
            "quantifiers": text.count("forall") + text.count("exists"),
            "array_ops": text.count("select") + text.count("store"),
            "fp_ops": text.count("fp.") + text.count("FloatingPoint"),
            "string_ops": text.count("str.") + text.count("String"),
        }

    models = list(dict.fromkeys(row["model"] for row in rows))
    by_model = {m: {r["benchmark"]: r for r in rows if r["model"] == m} for m in models}

    def aggregate(selected: list[dict]) -> dict:
        attempts = 5 * len(selected)
        verdict = sum(int(r["correct_verdicts"]) for r in selected)
        final = sum(int(r["final_successes"]) for r in selected)
        correct_sat = sum(int(r["correct_sat_verdicts"]) for r in selected)
        witness = sum(int(r["valid_sat_witnesses"]) for r in selected)
        return {"cases": len(selected), "attempts": attempts, "verdict": verdict,
                "final": final, "correct_sat": correct_sat, "witness": witness}

    md = []
    add = md.append
    add(f"# {args.batch} 大模型 CNF(T) 推理能力画像")
    add("")
    add("> 目标：识别模型倾向推理正确与难以推理的题型。统计基于 93 题、每模型每题 5 次。‘最终成功’=正确 UNSAT，或正确 SAT 且 witness 经 cvc5 验证。所有结论均是本批样本上的相关性，不是因果证明。")

    add("")
    add("## 1. 核心结论")
    add("")
    add("1. **最容易的是结构短、局部规律明显、无需复杂证书的题。** 三模型共同 15/15 的题往往 clause、literal 和文本规模较小，或者虽有理论运算但约束模式高度重复。")
    add("2. **最难的是理论组合与证书负担同时升高的 SAT 题。** 数组+整数算术、量词+算术，以及需要大量或精确类型赋值的 SAT，即使 verdict 正确，也经常在 witness 阶段失败。")
    add("3. **UNSAT 明显比 SAT 容易取得最终成功，但这部分来自实验规则。** UNSAT 只需命中 golden answer；SAT 还需产出完整模型并通过 cvc5，因此最终成功率不能被解释为纯分类能力。")
    add("4. **单纯 clause 数不是充分难度指标。** 规模与失败总体相关，但理论类型、量词、数组一致性、浮点精确表示、自由符号数量和最长 clause 共同决定实际难度。")
    add("5. **模型排名稳定：Codex 最强，Flash 次之，Pro 最弱。** 差距同时存在于 verdict 与 witness，不是某一个评分环节单独造成。")

    add("")
    add("## 2. 分类错误与证书错误分解")
    add("")
    add("‘分类失败’是 465 次中 verdict 不正确的次数；‘SAT 证书失败’只统计 verdict 已正确为 SAT、但 witness 未通过的次数。")
    add("")
    add("| 模型 | 分类成功 | 分类失败 | 正确 SAT | 有效 witness | SAT证书失败 | 最终成功 |")
    add("|---|---:|---:|---:|---:|---:|---:|")
    for model in models:
        a = aggregate(list(by_model[model].values()))
        add(f"| {model} | {a['verdict']}/{a['attempts']} ({percent(a['verdict'], a['attempts'])}) | {a['attempts']-a['verdict']} | {a['correct_sat']} | {a['witness']} | {a['correct_sat']-a['witness']} | {a['final']}/{a['attempts']} ({percent(a['final'], a['attempts'])}) |")

    add("")
    add("解释：分类成功并不保证最终成功。Codex 的主要剩余损失也集中在 SAT witness；DeepSeek 两个模型则同时受到分类错误和 witness 错误影响。")

    add("")
    add("## 3. SAT 与 UNSAT 倾向")
    add("")
    add("| 模型 | Golden | 题数 | Verdict accuracy | 最终成功率 | SAT witness rate |")
    add("|---|---|---:|---:|---:|---:|")
    for model in models:
        for status in ("sat", "unsat"):
            selected = [r for b, r in by_model[model].items() if features[b]["status"] == status]
            a = aggregate(selected)
            add(f"| {model} | {status} | {a['cases']} | {percent(a['verdict'], a['attempts'])} | {percent(a['final'], a['attempts'])} | {percent(a['witness'], a['correct_sat']) if status == 'sat' else '不适用'} |")
    add("")
    add("判断：如果题目是 UNSAT，模型只需识别矛盾；如果是 SAT，模型还要把存在性判断转化为完整赋值。SAT 的难点通常包括漏掉常量/函数、类型不合法、数组默认值不完整、浮点常量不精确，或赋值不能同时满足所有 clause。")

    add("")
    add("## 4. 理论类型维度")
    add("")
    add("| Logic | 题数 | Codex最终成功 | Flash最终成功 | Pro最终成功 | 综合判断 |")
    add("|---|---:|---:|---:|---:|---|")
    logic_notes = {
        "ABVFP": "分类较容易；DeepSeek 的精确浮点/位向量 witness 是瓶颈",
        "ALIA": "数组、整数和量词组合，分类与全局一致性推理更难",
        "LIA": "分类通常较好；量词/大整数关系使 SAT witness 明显变难",
        "NIA": "本样本规律性较强，表现好于‘非线性’名称所暗示的难度",
        "NRA": "分类稳定；少数 SAT 的实数 witness 构造仍会失败",
        "QF_ALIA": "主要 verdict 难点，数组与算术交互导致模型分化最大",
        "QF_AUFLIA": "主要 witness 难点，函数、数组 store/select 和整数需同时一致",
        "QF_NIRA": "仅 1 题，不能据此概括该逻辑",
        "QF_S": "字符串样本整体较稳，个别输出/构造存在波动",
    }
    for logic in sorted({f["logic"] for f in features.values()}):
        benchmarks = [b for b, f in features.items() if f["logic"] == logic]
        vals = []
        for model in models:
            selected = [by_model[model][b] for b in benchmarks]
            a = aggregate(selected)
            vals.append(f"{a['final']}/{a['attempts']} ({percent(a['final'], a['attempts'])})")
        add(f"| {logic} | {len(benchmarks)} | {' | '.join(vals)} | {logic_notes[logic]} |")

    # Global feature quartiles, identical thresholds across models.
    add("")
    add("## 5. 规模复杂度维度")
    add("")
    add("CNF(T) 难度不能用单一的文件长度代表。为了把‘公式为什么难’拆开，本报告把复杂度组织为四类：总体约束规模、分支复杂度、语义复杂度和证书复杂度。前三类影响模型判断 SAT/UNSAT 的推理负担，证书复杂度主要影响正确判断 SAT 后能否输出可被 cvc5 执行的完整模型。")
    add("")
    add("| 难度类别 | 对应指标 | 主要影响 | 典型失败方式 |")
    add("|---|---|---|---|")
    add("| 总体约束规模 | Clause 数、CNF 字符/字节数、原始 SMT2 字节数 | 模型需要读取、记住并联合检查多少内容 | 遗漏远距离约束，局部赋值与后部 clause 冲突 |")
    add("| 分支复杂度 | Literal 总数、最大/平均/中位 clause 宽度、单位子句数 | 模型需要在多少候选 literal 之间选择，并保持跨 clause 一致 | 选择了局部可行但全局冲突的分支 |")
    add("| 语义复杂度 | Logic、不同理论原子、量词、数组、字符串、算术、非线性、位向量、浮点和嵌套结构 | 每个原子的真假需要多复杂的理论推理 | 误解量词范围、数组一致性、非线性关系、位宽或浮点精确语义 |")
    add("| 证书复杂度 | 声明数、函数数、数组数、排序/值类型、预期 witness 大小 | SAT 时需要输出多大、多完整、多精确的模型 | 漏赋值、类型错误、函数/数组解释不完整或值不能满足全部约束 |")
    add("")
    add("这四类并非彼此独立。例如，clause 多通常也会增加 literal 和文本长度；数组题往往同时具有更多声明与更复杂的 witness。因此下列数据用于描述本批样本中的相关关系，不能单独证明某一指标造成失败。")
    add("")
    add("### 分桶方法")
    add("")
    add("对 93 题按每项数值的全局四分位数分箱，同一阈值用于三个模型，以便横向比较。由于相同数值不会被强行拆开，各箱题数可能不完全相等。表中展示的是最终成功率，因此同时包含 verdict 难度和 SAT witness 难度。")
    feature_names = [
        ("clauses", "Clause 数"), ("literals", "Literal 总数"),
        ("max_clause_literals", "最长 clause 的 literal 数"),
        ("chars", "CNF 字符数"), ("source_bytes", "原 SMT2 字节数"),
        ("declarations", "声明符号数"), ("quantifiers", "量词出现数"),
    ]
    for key, label in feature_names:
        values = [f[key] for f in features.values()]
        q1, q2, q3 = (quantile(values, q) for q in (0.25, 0.5, 0.75))
        ranges = [(f"≤{q1}", lambda x, q1=q1: x <= q1),
                  (f"{q1+1}–{q2}", lambda x, q1=q1, q2=q2: q1 < x <= q2),
                  (f"{q2+1}–{q3}", lambda x, q2=q2, q3=q3: q2 < x <= q3),
                  (f">{q3}", lambda x, q3=q3: x > q3)]
        add("")
        add(f"### {label}")
        add("")
        add("| 范围 | 题数 | Codex | Flash | Pro |")
        add("|---|---:|---:|---:|---:|")
        for range_label, predicate in ranges:
            benchmarks = [b for b, f in features.items() if predicate(f[key])]
            if not benchmarks:
                continue
            rates = []
            for model in models:
                a = aggregate([by_model[model][b] for b in benchmarks])
                rates.append(percent(a["final"], a["attempts"]))
            add(f"| {range_label} | {len(benchmarks)} | {' | '.join(rates)} |")
    add("")
    add("解释：如果随规模分箱单调下降，可视为该规模指标与难度相关；若不单调，通常说明箱内 logic 与 SAT/UNSAT 构成不同。尤其量词数为 0 并不保证简单——QF_AUFLIA、QF_ALIA 虽无量词，理论组合仍然困难。")

    add("")
    add("## 6. 稳定性：会不会做与能否稳定做")
    add("")
    add("| 模型 | 稳定成功 5/5 | 较稳定 4/5 | 边界 2–3/5 | 偶发 1/5 | 稳定失败 0/5 |")
    add("|---|---:|---:|---:|---:|---:|")
    for model in models:
        counts = Counter(int(r["final_successes"]) for r in by_model[model].values())
        add(f"| {model} | {counts[5]} | {counts[4]} | {counts[2]+counts[3]} | {counts[1]} | {counts[0]} |")
    add("")
    add("5/5 表示模型不仅能找到思路，而且输出协议和证书构造稳定；2/5～3/5 表示已靠近能力边界，采样会改变结果；0/5 更可能是系统性推理缺口、持续的证书表达缺口，或提示表示对该题型不友好。")

    # Compare model wins and shared hard/easy.
    totals = {b: {m: int(by_model[m][b]["final_successes"]) for m in models} for b in features}
    shared_easy = sorted(b for b, x in totals.items() if sum(x.values()) == 15)
    shared_hard = sorted(b for b, x in totals.items() if sum(x.values()) == 0)
    unique_best = Counter()
    for scores in totals.values():
        best = max(scores.values())
        winners = [m for m, value in scores.items() if value == best]
        if len(winners) == 1:
            unique_best[winners[0]] += 1
    add("")
    add("## 7. 模型间差异")
    add("")
    add(f"- 三模型共同稳定成功：{len(shared_easy)} 题；共同稳定失败：{len(shared_hard)} 题。")
    add("- 单题最终成功次数严格领先的题数：" + "；".join(f"{m} {unique_best[m]} 题" for m in models) + "。")
    add("- Codex 的优势是跨 logic 的稳定性以及更完整的 SAT witness；Flash 的主要优势是相对 Pro 更可靠的 verdict 与证书；Pro 在本批次不是‘更慢但更准’，其实际正确率反而最低，说明模型名称不能替代同配置实测。")
    add("")
    add("共同 0/15 用例：")
    add("")
    for benchmark in shared_hard:
        f = features[benchmark]
        add(f"- `{benchmark}`：{f['status']}, {f['logic']}, {f['clauses']} clauses, {f['literals']} literals, {f['declarations']} declarations, {f['quantifiers']} quantifiers")

    add("")
    add("## 8. 什么样的题倾向推理正确")
    add("")
    add("综合本批数据，以下特征提高成功倾向：")
    add("")
    add("- clause 和 literal 较少，最长 clause 不需要同时追踪大量分支；")
    add("- 约束具有重复的局部模板，可以通过模式匹配快速确定矛盾或构造赋值；")
    add("- 单一理论为主，跨数组、函数、算术、浮点的交互较少；")
    add("- UNSAT 矛盾核心明显，不要求输出机器可验证的反证；")
    add("- SAT 时自由符号少、赋值短、整数或字符串值容易精确表达；")
    add("- 五次运行都能复现相同判断和完整 JSON/证书结构。")

    add("")
    add("## 9. 什么样的题很难推理")
    add("")
    add("困难通常不是由一个指标单独决定，而是四类复杂度发生叠加。可以把风险理解为：模型既要处理足够大的约束集合，又要搜索分支、正确解释理论语义，并在 SAT 时把推理结果完整编码成证书。")
    add("")
    add("| 风险来源 | 高风险特征 | 为什么困难 | 本实验中的信号 |")
    add("|---|---|---|---|")
    add("| 总体约束规模 | clause、CNF 文本和原始 SMT2 同时较大 | 需要跨更长距离保持变量、原子和约束一致，容易只满足局部公式 | clause >46 时三模型成功率均下降；原 SMT2 >5720 字节时 Flash/Pro 降幅尤其明显 |")
    add("| 分支复杂度 | literal 总数高、多个宽 clause 相互耦合 | 每个 clause 的局部选择会限制其他 clause，组合搜索空间扩大 | literal >82 时 Codex/Flash/Pro 分别为 78.26%/51.30%/32.17% |")
    add("| 语义复杂度 | 数组+函数+整数、量词+算术、非线性、位向量/浮点精确语义 | 不能只按布尔外壳推理，必须理解理论原子内部的真实语义 | QF_ALIA 是突出 verdict 难点；ABVFP 中 DeepSeek 的 witness 明显弱于其分类 |")
    add("| 证书复杂度 | SAT、声明多、包含函数/数组、值类型复杂 | 正确判断 SAT 后仍需覆盖全部自由符号并满足类型和全局约束 | 声明 >20 时 Codex/Flash/Pro 分别为 64.76%/39.05%/28.57%；共同 0/15 的 8 题全部为 SAT |")
    add("")
    add("### 四类典型困难")
    add("")
    add("1. **规模大但语义简单：容易遗漏，不一定不会推理。** 大量重复 clause 会拉长输入并增加核对负担。模型可能掌握局部规律，却漏掉少数例外约束。")
    add("2. **规模小但语义很深：不能依据短公式判断容易。** 一个 clause 内可以包含量词、非线性等式或复杂数组原子。共同失败的 `NRA/722eaea277-strassen-hard.md` 只有 1 个外层 clause，却仍是三模型 0/15。")
    add("3. **分支多且跨 clause 耦合：容易得到局部解。** 某个 literal 单独可真，不代表选它后其余 clause 仍有一致赋值；最长 clause 本身也不呈单调难度，因为宽析取有时反而容易满足。")
    add("4. **判断正确但证书复杂：属于表达/构造失败。** 这在 SAT 数组、函数和浮点题中尤其常见。它不应与 verdict 错误混为一类，而应通过 `sat_witness_valid` 和验证器错误进一步区分。")
    add("")
    add("### 最高风险组合")
    add("")
    add("本批数据中，最危险的组合是：**SAT + 大量 clause/literal + 超过 20 个声明 + 数组或函数与整数算术组合**。这类题同时提高总体规模、分支、理论语义和证书四方面负担。QF_AUFLIA 的共同失败题分别出现 35、53、85、245 个声明，说明其失败不能只归结为 CNF 长度。")
    add("")
    add("另一类风险是：**外层 CNF 很短，但理论原子内部包含量词或非线性全局条件**。如果只统计换行数或外层括号，会低估这类题。因此后续复杂度解析必须正确识别 `⟦...⟧` 边界，并分别统计理论原子数量、长度、理论类型和嵌套程度。")
    add("")
    add("2/5～3/5 的题表示模型在当前提示和采样条件下处于能力边界：有时能找到有效推理或证书，有时失败。0/5 且三模型共同失败更接近系统性难题，但仍需检查失败究竟来自 verdict、JSON/类型表达还是 cvc5 判定 witness 不满足。")

    add("")
    add("## 10. 综合能力边界与实验建议")
    add("")
    add("当前实验支持的最稳妥结论是：大模型已经能可靠处理一批规模较小或结构规律明显的 CNF(T)，也能在某些非线性和字符串样本上表现很好；但当理论组合、全局依赖和机器可执行 witness 负担同时增大时，性能显著下降。‘会判断 SAT’与‘会构造一个真正模型’是两种不同能力，必须继续分别报告。")
    add("")
    add("下一批建议按 logic 和 golden status 分层，再分别控制 clause 数、literal 数、最长 clause、声明数、量词数与预期 witness 大小。每个区间应有足够样本，否则规模和理论类型会互相混杂。还应记录 cvc5 的证书失败类别（缺符号、解析失败、类型错误、约束不满足、超时），这样才能判断模型到底是不会推理，还是会推理但不会按协议表达。")

    output.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
