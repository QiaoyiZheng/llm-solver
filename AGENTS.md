# 大模型 CNF 推理能力评测说明

本项目用于评测大模型直接判断谓词逻辑 CNF 公式可满足性的能力，并分析模型能够处理的 CNF 复杂度范围。

## 实验对象

必须评测以下三个模型：

- Codex：调用本机已安装的 `codex.cmd`/`codex exec`；
- DeepSeek V4 Flash：API 模型 ID 为 `deepseek-v4-flash`；
- DeepSeek V4 Pro：API 模型 ID 为 `deepseek-v4-pro`。

DeepSeek API 使用 OpenAI 兼容端点 `https://api.deepseek.com/chat/completions`。API key 只能从环境变量 `DEEPSEEK_API_KEY` 读取，禁止写入代码、配置、日志、提示词或 Git。

## 评测输入

- CNF 输入位于 `benchmarks/CNF-Bench/`；
- 目录按 SMT-LIB logic 分类；
- 每个 `.md` 文件只包含一个 CNF(T) 数学表达式；
- `⟦φ⟧` 表示保留语义的理论原子，其真假与内部谓词公式 `φ` 相同；
- `τN` 和 `λN` 是转换时引入的辅助符号；
- 不得修改 `benchmarks/CNF-Bench/`、`benchmarks/smtlib-2025/` 或 manifest。

这里评测的是 CNF(T)，不是仅含布尔变量的纯命题 CNF。模型需要考虑理论原子中的整数、实数、数组、字符串、位向量、浮点数和量词语义。

## 标准答案与标签隔离

标准答案来自 `benchmarks/smtlib-2025/manifest.json` 中对应原始 `.smt2` 文件的 `status`。

必须严格隔离推理与评分：

1. 调用模型时，只传入统一任务说明和 CNF 表达式；
2. 禁止向模型传入 manifest、标准答案、原始文件名、目录路径、checksum、source、status 或历史评分结果；
3. 禁止根据文件名中的 `sat`、`unsat`、`true`、`false` 等文字推断答案；
4. 模型完成回答后，评分程序才能读取标准答案并比较；
5. 结果文件可以在评分阶段记录 benchmark ID 和标准答案，但这些字段不得进入模型请求。

## 直接推理约束

模型只能根据提示词中的 CNF 表达式直接推理：

- 禁止调用 cvc5、Z3、SAT/SMT 求解器或任何外部判定器；
- 禁止联网搜索答案；
- 禁止读取 benchmark、manifest 或项目中的其他文件；
- 禁止编写或运行脚本来代替逻辑推理；
- 每次调用必须是全新的独立会话，不得共享前一次运行的上下文或答案。

Codex 必须使用临时独立工作目录、ephemeral 会话和只读 sandbox。运行器应审计 Codex JSONL 事件；若发生 shell、MCP、网页或其他工具调用，该次结果标记为 `contaminated`，不得计为有效的直接推理结果。

DeepSeek 必须启用 thinking mode，并固定 `reasoning_effort=max`。thinking mode 下不要设置无效的 `temperature`、`top_p`、`presence_penalty` 或 `frequency_penalty`。不得给 DeepSeek 提供 tools。

## 统一证书输出协议

三个模型使用完全相同的任务语义，只允许最终输出一个 JSON 对象。SAT 必须提供完整模型见证：

```json
{"schema_version":1,"status":"sat","certificate":{"kind":"sat_model","constants":[],"functions":[]}}
```

`status` 只能是：

- `sat`
- `unsat`
- `unknown`

UNSAT 不要求证明，必须输出 `certificate.kind=none`：

```json
{"schema_version":1,"status":"unsat","certificate":{"kind":"none"}}
```

模型输出无法严格解析时，记录为 `invalid`，不得猜测或从长篇回答中宽松提取答案。

## 证书实验输入

除状态分类 baseline 外，项目必须提供证书实验。证书实验的模型可见输入位于
`benchmarks/certificate-inputs/cases/`，每个 JSON 只能包含：

- `schema_version`；
- `logic`；
- 原始 SMT-LIB 符号的结构化 `declarations`；
- CNF(T) 数学表达式 `cnf`。

JSON 中禁止出现 case ID、原始文件名、路径、expected status、checksum、source、
manifest 字段或历史结果。case ID 只能作为 opaque 文件名存在，且不能加入模型 prompt。
证书运行器可以把整个 JSON 内容发送给模型，但不能发送该文件的路径或文件名。

SAT 结果必须附带覆盖全部原始自由符号的可机验见证；验证器把见证编译成 SMT-LIB
后与原公式一起检查。部分赋值不能算完整证书，因为求解器可能自动补全缺失符号。
UNSAT 只比较模型分类与私有 golden answer；两者均为 `unsat` 时即分类正确，不调用
cvc5 验证 UNSAT 证明。

每次实验必须记录 `verdict_correct`、`sat_witness_checked`、
`sat_witness_valid` 和 `verification_basis`。项目只汇总两个核心比例指标：

1. SAT/UNSAT accuracy = 五次运行中所有分类正确次数 / 所有有效运行次数；
2. SAT 真解率 = cvc5 验证有效的 SAT 见证数 / 分类正确的 SAT 回答数。

正确 UNSAT 只进入指标 1，不进入 SAT 真解率的分子或分母。

## 重复次数与正确性

- 每个模型对每个 benchmark 必须完成 5 次有效、相互独立的运行；
- API、网络、超时或进程错误属于基础设施失败，不占用 5 次有效运行名额，应重试并单独记录；
- `invalid` 是一次有效模型响应，但判为错误；
- `contaminated` 不属于有效直接推理，必须补跑；
- 预测值与 manifest 的 `status` 完全相同时才算正确；
- 对标准答案为 `sat` 或 `unsat` 的题目，回答 `unknown` 算错误；
- 禁止多数投票替代单次统计。

准确率必须让五次独立运行逐次参与计算，禁止先多数投票再按题计分。

另外，每个 benchmark、每个模型必须得到一个“最终成功次数”：正确 UNSAT 算成功；
SAT 只有分类正确且见证通过 cvc5 才算成功。该计数取值为 5、4、3、2、1、0，报告
必须列出每档题目数量、比例和具体题目。没有跑满五次的题必须单列 incomplete，禁止
当作 0/5。

## 统计批次规范

- 统计快照统一存放在 `experiments/statistics/vN/`，从 `v1` 递增；
- 每轮新实验对应一个新的统计批次，禁止覆盖已经发布的旧批次；
- 每批必须包含来源运行目录与配置、模型汇总、logic 汇总、逐题明细、0/5～5/5
  分布和每档具体题目清单；
- 标准文件为 `manifest.json`、`summary.json`、`models.csv`、`logics.csv`、
  `cases.csv`、`distributions.csv`、`success_buckets.csv` 和
  `success_buckets.json`；
- 统计前按 `(case, run)` 去重，只保留最新 attempt；基础设施重试不得重复计分；
- SAT/UNSAT accuracy 对全部五次有效回答做 micro-average，不使用多数投票；
- `success_buckets` 使用“正确 UNSAT 或正确 SAT 且见证有效”的最终成功定义。
- 每批若排除 benchmark，必须在 `experiments/benchmark-sets/vN.json` 中列出 opaque
  case、原因和统一适用规则；三个模型必须使用同一集合，禁止只从某个模型分母删除；
- v2 的正式集合为 93 题，每模型 465 个槽位，具体排除项见
  `experiments/benchmark-sets/v2.json`。原始响应必须保留。

## 可复现运行要求

评测程序必须：

- 支持中断后续跑，不重复已经完成的有效运行；
- 每次响应立即追加写入结果，避免长实验中途丢失；
- 保存模型名、模型实际返回名称（如果 API 提供）、run 序号、时间戳、耗时、预测、正确性、finish reason、token usage 和错误类型；
- 保存 prompt 模板版本或哈希；
- 记录 Codex CLI 版本及使用的模型配置；
- 设置明确超时并实现有限次数、带退避的基础设施重试；
- 默认禁止把付费 API 的全量实验作为普通测试自动运行；
- 提供按模型、logic、benchmark 数量筛选的 pilot 运行方式；
- 原始响应、实验日志和生成报告写入 Git 忽略的实验输出目录，不得混入 benchmark 目录。

禁止静默覆盖已有实验结果。改变提示词、模型、thinking 设置、推理强度或输出协议时，必须使用新的 experiment ID。

## CNF 复杂度指标

分析不能只使用文件大小。至少为每个 benchmark 统计：

- logic 类别；
- UTF-8 字节数和字符数；
- 子句数；
- 文字总数；
- 不同理论原子数；
- Tseitin 辅助变量数；
- 单位子句数；
- 最大、平均和中位子句宽度；
- 理论原子的平均和最大字符长度；
- 量词、数组、字符串、整数/实数算术、非线性算术、位向量和浮点相关特征；
- 公式嵌套或其他可稳定复现的结构指标。

复杂度解析必须识别 `⟦...⟧` 的边界，不能把理论原子内部的 `∧`、`∨` 或括号误当成外层 CNF 结构。

## 结果报告

完成全量实验后，至少生成以下内容：

1. 每题明细：三个模型各自的 5 次预测、分类正确次数、最终成功次数和 5/4/3/2/1/0 分组；
2. 模型汇总：SAT/UNSAT accuracy、SAT 真解率、有效运行数、invalid 数和基础设施失败数；
3. logic 汇总：每个模型在各 logic 上的准确率和正确次数分布；
4. 复杂度分桶：按子句数、文字数、最大子句宽度、理论原子长度等分位数分桶；
5. 稳定性分析：区分稳定正确（5/5）、不稳定（4/5 至 1/5）和稳定错误（0/5）；
6. `sat` 与 `unsat` 分开分析，避免类别比例掩盖差异；
7. Codex、V4 Flash、V4 Pro 的成对比较；
8. 对“模型能处理什么复杂度”给出有数据支持的结论，并报告样本数量和失败类型。

不要把相关性描述成因果关系。样本只有 95 题且来自特定 SMT-LIB 子集，结论必须限定在本实验数据范围内。

## 工作流程

1. 校验 95 个 CNF 文件与 manifest 一一对应，但不把标签加入 prompt；
2. 固定并记录 prompt 版本、模型配置和 experiment ID；
3. 先用少量不同 logic 的 benchmark 做 pilot，验证解析、超时、标签隔离和结果落盘；
4. 分别运行 Codex、DeepSeek V4 Flash、DeepSeek V4 Pro；
5. 确认每个模型每题均有 5 次有效运行；
6. 生成统计表和复杂度分析；
7. 抽查原始响应、invalid、contaminated 和异常样本；
8. 报告实验配置、完成度、成本/耗时、限制以及最终结论。
