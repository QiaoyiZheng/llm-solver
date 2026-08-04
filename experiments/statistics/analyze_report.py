#!/usr/bin/env python3
"""Build the human-readable analysis report for a completed statistics batch."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def pct(numerator: int, denominator: int) -> str:
    return f"{100 * numerator / denominator:.2f}%" if denominator else "—"


def median(values: list[int]) -> str:
    return f"{statistics.median(values):.0f}" if values else "—"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch", nargs="?", default="v2")
    args = parser.parse_args()
    stats_dir = ROOT / "experiments" / "statistics" / args.batch
    out_dir = stats_dir / "analyze"
    out_dir.mkdir(parents=True, exist_ok=True)

    summary = load_json(stats_dir / "summary.json")
    manifest = load_json(stats_dir / "manifest.json")
    buckets = load_json(stats_dir / "success_buckets.json")["models"]
    source_manifest = load_json(ROOT / "benchmarks" / "smtlib-2025" / "manifest.json")
    source_by_md = {
        item["path"].removesuffix(".smt2") + ".md": item
        for item in source_manifest["benchmarks"]
    }

    with (stats_dir / "cases.csv").open(encoding="utf-8-sig", newline="") as handle:
        case_rows = list(csv.DictReader(handle))

    details: dict[str, dict] = {}
    for row in case_rows:
        benchmark = row["benchmark"]
        if benchmark in details:
            continue
        cnf_path = ROOT / "benchmarks" / "CNF-Bench" / benchmark
        text = cnf_path.read_text(encoding="utf-8")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        source = source_by_md[benchmark]
        details[benchmark] = {
            "logic": row["logic"],
            "status": source["status"],
            "clauses": len(lines),
            "literals": sum(line.count("∨") + 1 for line in lines),
            "cnf_chars": len(text),
            "source_bytes": source["size"],
            "quantifiers": text.count("forall") + text.count("exists"),
            "arrays": text.count("select") + text.count("store"),
            "fp_ops": text.count("fp.") + text.count("FloatingPoint"),
        }

    rows_by_model = defaultdict(dict)
    for row in case_rows:
        rows_by_model[row["model"]][row["benchmark"]] = row

    lines: list[str] = []
    add = lines.append
    add(f"# {args.batch} 实验分析报告")
    add("")
    add("> 本报告基于完整的 93 个测试用例 × 3 个模型 × 5 次重复实验。最终成功定义为：正确 UNSAT，或正确 SAT 且模型 witness 通过 cvc5。SAT/UNSAT Accuracy 只看分类；SAT witness rate 只在分类正确的 SAT 回答中计算。")
    add("")
    add("## 1. 实验范围与总体结果")
    add("")
    add(f"- 批次状态：`{manifest['batch_status']}`；每模型 {manifest['planned_cases_per_model']} 题、{manifest['planned_slots_per_model']} 次。")
    add(f"- 排除用例：{', '.join(f'`{x}`' for x in manifest['excluded_cases'])}（统一对三个模型排除）。")
    add("")
    add("| 模型 | 完成 | SAT/UNSAT 正确 | Accuracy | 有效 SAT witness | 正确 SAT | Witness rate | 正确 UNSAT |")
    add("|---|---:|---:|---:|---:|---:|---:|---:|")
    for model in summary["models"]:
        acc = model["sat_unsat_accuracy"]
        wit = model["sat_witness_rate"]
        add(f"| {model['model']} | {model['completed_slots']}/{model['planned_slots']} | {acc['numerator']}/{acc['denominator']} | {pct(acc['numerator'], acc['denominator'])} | {wit['numerator']} | {wit['denominator']} | {pct(wit['numerator'], wit['denominator'])} | {model['correct_unsat']} |")

    add("")
    add("### 最终成功次数分布")
    add("")
    add("| 模型 | 5/5 | 4/5 | 3/5 | 2/5 | 1/5 | 0/5 |")
    add("|---|---:|---:|---:|---:|---:|---:|")
    for model, model_buckets in buckets.items():
        add("| " + model + " | " + " | ".join(str(len(model_buckets[str(i)])) for i in range(5, -1, -1)) + " |")

    add("")
    add("### 按逻辑的指标")
    add("")
    add("| 模型 | 逻辑 | Accuracy | SAT witness rate |")
    add("|---|---|---:|---:|")
    with (stats_dir / "logics.csv").open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            witness = pct(int(row["valid_sat_witnesses"]), int(row["correct_sat_verdicts"]))
            add(f"| {row['model']} | {row['logic']} | {pct(int(row['accuracy_correct']), int(row['accuracy_total']))} | {witness} |")

    add("")
    add("## 2. 各模型 0/5～5/5 用例汇总")
    add("")
    add("下列分桶依据最终成功，而不是只看 SAT/UNSAT 分类。每项格式为 `逻辑/文件名 [golden, clauses, CNF字符数]`。")
    for model, model_buckets in buckets.items():
        add("")
        add(f"### {model}")
        for score in range(5, -1, -1):
            items = model_buckets[str(score)]
            add("")
            add(f"#### {score}/5（{len(items)} 题）")
            add("")
            if not items:
                add("无。")
                continue
            for item in items:
                d = details[item["benchmark"]]
                add(f"- `{item['benchmark']}` [{d['status']}, {d['clauses']} clauses, {d['cnf_chars']} chars]")

    # Cross-model agreement and difficulty.
    total_success = Counter()
    for model, by_benchmark in rows_by_model.items():
        for benchmark, row in by_benchmark.items():
            total_success[benchmark] += int(row["final_successes"])
    all_easy = sorted(b for b, score in total_success.items() if score == 15)
    all_hard = sorted(b for b, score in total_success.items() if score == 0)
    mixed = sorted(total_success, key=lambda b: (total_success[b], b))

    add("")
    add("## 3. 三模型共同能力边界")
    add("")
    add(f"- 三模型全部 15/15 成功：{len(all_easy)} 题。")
    add(f"- 三模型全部 0/15 成功：{len(all_hard)} 题。")
    add("- 其余题存在模型差异或重复运行波动；总成功次数越靠近 7～8/15，越接近当前模型族的经验能力边界。")
    add("")
    add("### 共同稳定可解（15/15）")
    add("")
    add(", ".join(f"`{b}`" for b in all_easy) or "无。")
    add("")
    add("### 共同完全失败（0/15）")
    add("")
    add(", ".join(f"`{b}`" for b in all_hard) or "无。")
    add("")
    add("### 全部用例的跨模型总成功次数")
    add("")
    add("| 总成功/15 | 题数 | 用例 |")
    add("|---:|---:|---|")
    by_total = defaultdict(list)
    for benchmark in mixed:
        by_total[total_success[benchmark]].append(benchmark)
    for score in range(15, -1, -1):
        items = by_total[score]
        if items:
            add(f"| {score} | {len(items)} | " + ", ".join(f"`{x}`" for x in items) + " |")

    add("")
    add("## 4. 复杂度与结构因素分析")
    add("")
    add("这里的 clause 数是 CNF-Bench 文件的非空行数；literal 数按每行析取项估算。它们衡量表示规模，但不能完整代表理论推理难度。下表按三模型合计成功次数分组。")
    add("")
    add("| 跨模型成功组 | 题数 | clauses 中位数 | literals 中位数 | CNF字符中位数 | SMT2字节中位数 | 量词出现中位数 |")
    add("|---|---:|---:|---:|---:|---:|---:|")
    bands = [("稳定（15/15）", lambda s: s == 15), ("较强（10–14/15）", lambda s: 10 <= s <= 14), ("边界（5–9/15）", lambda s: 5 <= s <= 9), ("困难（0–4/15）", lambda s: s <= 4)]
    for label, pred in bands:
        selected = [details[b] for b, score in total_success.items() if pred(score)]
        add(f"| {label} | {len(selected)} | {median([d['clauses'] for d in selected])} | {median([d['literals'] for d in selected])} | {median([d['cnf_chars'] for d in selected])} | {median([d['source_bytes'] for d in selected])} | {median([d['quantifiers'] for d in selected])} |")

    # status and logic final success summaries
    add("")
    add("### Golden status 与理论类型")
    add("")
    add("| 维度 | 用例数 | 最终成功次数 | 最大次数 | 成功率 |")
    add("|---|---:|---:|---:|---:|")
    dimensions = defaultdict(list)
    for benchmark, score in total_success.items():
        d = details[benchmark]
        dimensions[f"status={d['status']}"].append(score)
        dimensions[f"logic={d['logic']}"].append(score)
    for key in sorted(dimensions):
        vals = dimensions[key]
        add(f"| {key} | {len(vals)} | {sum(vals)} | {15 * len(vals)} | {pct(sum(vals), 15 * len(vals))} |")

    add("")
    add("### 结论与原因解释")
    add("")
    add("1. **Codex 在分类和证书两个阶段都最稳定。** 它的 Accuracy 为 96.56%，SAT witness rate 为 80.84%；Flash 分别为 86.67% 与 73.54%，Pro 为 76.56% 与 63.64%。因此模型间差距不只是 SAT/UNSAT 判断，也来自把 SAT 推理落实为可执行赋值的能力。")
    add("2. **UNSAT 与 SAT 的评分非对称。** UNSAT 命中 golden answer 即成功，而 SAT 还必须产生完整、语法正确且满足全部约束的 witness。因此 SAT 题的最终成功率天然同时受分类、模型构造、类型编码和 cvc5 校验影响；不能把 SAT 失败全部解释成逻辑判断失败。")
    add("3. **理论结构比单纯 clause 数更关键。** QF_AUFLIA 同时涉及数组、整数线性算术以及 store/select 一致性，多个模型即使判断 SAT 正确，也容易遗漏数组默认值或索引关系；LIA 中带量词或需要构造大量整数关系的题也会降低 witness 成功率。相反，部分 clause 很多但局部约束规律重复的题仍可能稳定成功。")
    add("4. **QF_ALIA 是主要分类弱点之一。** 三模型该逻辑 Accuracy 明显分化，说明数组与线性整数算术组合不仅影响 witness，也影响 verdict。ALIA 中的量词进一步增加全称条件与有限 witness 之间的推理负担。")
    add("5. **NRA/NIA 的表现说明‘非线性’不必然等于失败。** 本样本中的 NRA 分类非常稳定，NIA 也相对较好；这更可能反映所抽取实例具有可识别结构或容易构造的解，而不是模型已普遍掌握任意非线性算术。结论不能外推到整个 SMT-LIB 分布。")
    add("6. **浮点/位向量的主要风险在精确编码。** ABVFP 中分类通常较准，但 DeepSeek 尤其 Pro 的 witness rate 较低，常见瓶颈是浮点特殊值、舍入模式、位宽与精确常量格式，而不是只看公式长度。")
    add("7. **重复运行波动是重要信号。** 3/5、2/5 一类题表示模型已有部分能力但推理链或输出格式不稳定；0/5 且三模型共同失败的题才更像当前提示与输出协议下的系统性能力缺口。")

    add("")
    add("## 5. 最终判断")
    add("")
    add("在当前 93 题样本上，模型最可靠的是结构规律明显、赋值规模有限、证书容易完整表达的 CNF(T)；最不可靠的是数组与整数算术组合、带量词的全局约束，以及需要精确浮点/大规模数组 witness 的 SAT 题。Codex 5.6 Sol 的能力边界最宽，DeepSeek V4 Flash 次之，V4 Pro 在本批配置下最弱。复杂度不能仅用 clause 数排序：理论组合、量词、需要赋值的符号数量、精确数值编码和重复结构，都会显著改变难度。")
    add("")
    add("报告中的相关性是对本批 93 题的描述性分析，不构成因果证明。后续批次应在每种 logic 内按 clause、符号数、量词深度与 witness 大小分层采样，才能更严格地估计大模型可处理的复杂度阈值。")

    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_dir / "report.md")


if __name__ == "__main__":
    main()
