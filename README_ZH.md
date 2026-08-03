# 大模型 CNF(T) 可验证求解实验

本项目用于评估大模型能否直接求解谓词逻辑 CNF(T) 公式，并给出可以由程序执行和验证的证书。证书实验是目前唯一的默认实验，不再单独运行只输出 `sat/unsat` 的普通分类 baseline。

英文文档：[README.md](README.md)

## 评测模型

- Codex：`gpt-5.6-sol`，`high` 推理强度，Priority 服务档位；如果 CLI 提供，则保存 detailed reasoning summary。
- DeepSeek V4 Flash：`deepseek-v4-flash`，启用 thinking，固定 `reasoning_effort=max`。
- DeepSeek V4 Pro：`deepseek-v4-pro`，启用 thinking，固定 `reasoning_effort=max`。

每个模型对每道题独立运行 5 次。API、网络、超时和进程错误属于基础设施错误，需要重试且不占 5 次有效名额。模型返回了响应但 JSON 格式错误时，属于一次有效但错误的模型结果。

## 项目目录说明

```text
llm-solver/
|-- AGENTS.md
|-- README.md
|-- README_ZH.md
|-- api-key                         # 本地密钥，Git 忽略
|-- benchmarks/
|   |-- smtlib-2025/                # 原始 SMT-LIB 和私有 manifest
|   |-- CNF-Bench/                  # 按 logic 分类的数学 CNF(T)
|   |-- certificate-inputs/         # 模型可见的无标签 JSON
|   `-- smoke/                      # 小型基础设施测试样例
|-- experiments/
|   |-- certificate-verifier/       # 证书 Schema、验证器和测试
|   |-- codex-gpt-5.6-sol/          # Codex 配置、runner 和结果
|   |-- deepseek-v4-flash/          # Flash 配置、runner 和结果
|   |-- deepseek-v4-pro/            # Pro 配置、runner 和结果
|   |-- check_deepseek_config.py    # 不泄漏密钥的 API 检查
|   |-- smoke_test.py               # 单次端到端诊断脚本
|   `-- CERTIFICATE_EXPERIMENT_PROPOSAL.md
`-- tools/
    `-- cvc5/                       # 固定版本的本地证书裁判
```

### 根目录文件

- `AGENTS.md`：项目长期实验规则，包括标签隔离、禁止模型使用工具、每题 5 次、证书评分和报告要求。
- `README.md`：英文项目说明与完整验证流程。
- `README_ZH.md`：中文项目说明与完整验证流程。
- `.gitignore`：忽略 API 密钥、Python 缓存和实验运行产物。
- `api-key`：本机 DeepSeek 密钥，不得提交、复制到实验快照或输出到日志。

### `benchmarks/`

- `smtlib-2025/`：原始 `.smt2` 公式；其中 `manifest.json` 保存私有标准状态和来源信息，模型绝不能读取。
- `CNF-Bench/`：每道题对应一个 `.md` 数学 CNF(T) 表达式，按照 SMT-LIB logic 分类。它是转换结果，实验期间不得修改。
- `certificate-inputs/cases/`：实际发送给模型的 95 个 opaque、无标签 JSON 输入。
- `certificate-inputs/schema/certificate-input.schema.json`：模型输入格式定义。
- `certificate-inputs/scripts/build_inputs.py`：根据私有 SMT-LIB/CNF 对应关系重新生成并审计 95 个公开输入。
- `certificate-inputs/README.md`：说明哪些字段可以发送给模型、哪些字段必须隔离。
- `smoke/`：少量已知 SAT/UNSAT 的本地基础设施样例，不属于 95 道正式大模型评测语料。

### `experiments/`

- `certificate-verifier/schema/certificate-response.schema.json`：三个模型共同遵守的证书输出格式。
- `certificate-verifier/scripts/verify_certificate.py`：严格解析模型输出，构造 SAT/UNSAT 检查并调用 cvc5。
- `certificate-verifier/tests/test_verifier.py`：验证器的合成用例和真实 benchmark 回归测试。
- `codex-gpt-5.6-sol/config/prompt.txt`：当前三个模型共同使用的证书任务 prompt。
- `codex-gpt-5.6-sol/scripts/run_codex.py`：调用 Codex、审计工具污染、保存事件和 reasoning summary、执行分类门控及证书验证。
- `deepseek-v4-flash/config/api.json`、`deepseek-v4-pro/config/api.json`：不含密钥的 endpoint、模型 ID 和密钥文件相对路径配置。
- 两个 DeepSeek `scripts/run_certificate.py`：负责五次重复、并发 API 请求、基础设施重试、分类门控、cvc5 验证和断点续跑。Pro wrapper 复用 Flash 的通用实现并替换为 Pro 配置。
- `check_deepseek_config.py`：在不打印密钥的情况下检查密钥加载；可选检查只读 `/models` 接口。
- `smoke_test.py`：每个指定模型只调用一次的真实端到端诊断。其结果不能混入正式全量统计。
- `CERTIFICATE_EXPERIMENT_PROPOSAL.md`：记录证书格式、评分语义以及未来 Alethe/LRAT 强证明扩展。
- `<模型>/runs/`：被 Git 忽略的时间戳实验产物；内部文件见后文“实验目录和产物”。

### `tools/cvc5/`

- `README.md`：记录固定 cvc5 版本、官方下载来源和 SHA-256。
- `1.3.3/.../bin/cvc5.exe`：验证器实际调用的可执行文件。
- `COPYING`、`AUTHORS` 和 `licenses/`：上游许可证与作者声明。
- 本地 SDK 头文件、静态库、JNI 和 Java 文件不被 Python 实验使用，而且部分文件超过 GitHub 大文件限制，因此不提交 Git。

## 输入与标签隔离

原始 SMT-LIB benchmark 和私有标签位于 `benchmarks/smtlib-2025/`，数学 CNF(T) 表达式位于 `benchmarks/CNF-Bench/`。

模型只能看到 `benchmarks/certificate-inputs/cases/` 中的 JSON：

```json
{
  "schema_version": 1,
  "logic": "LIA",
  "declarations": [],
  "cnf": "(...)"
}
```

模型输入中不得包含标准答案、manifest、source、checksum、原始文件名、路径或历史结果。opaque case 文件名也不能加入 prompt。只有模型完成回答后，评分程序才能根据 CNF 内容恢复私有 benchmark 对应关系并读取标准答案。

## 模型输出协议

模型只能输出一个 JSON 对象，不能附带 Markdown 或解释文字。

SAT 必须解释全部原始声明：

```json
{
  "schema_version": 1,
  "status": "sat",
  "certificate": {
    "kind": "sat_model",
    "constants": [
      {"symbol": "x", "sort": "Int", "value_smt2": "2"}
    ],
    "functions": []
  }
}
```

UNSAT 必须给出从 1 开始编号的非空矛盾子句集合：

```json
{
  "schema_version": 1,
  "status": "unsat",
  "certificate": {
    "kind": "unsat_core",
    "clause_indices": [1, 4, 7]
  }
}
```

无法可靠给出结论和证书时，可以输出：

```json
{"schema_version":1,"status":"unknown","certificate":{"kind":"none"}}
```

对于标准答案为 SAT 或 UNSAT 的题目，`unknown` 计为错误。

## 完整验证流程

评分必须严格按照以下顺序进行：

1. 读取一个无标签 certificate case。
2. 只把 JSON 内容放入 prompt，不发送文件名或路径。
3. 为模型建立全新独立会话；禁止模型调用工具、求解器、网络或历史上下文。
4. 在评分前保存模型原始响应和接口提供的 reasoning 数据。
5. 严格读取顶层 `status`，只能是 `sat`、`unsat` 或 `unknown`。
6. 根据 CNF 内容恢复私有原始 benchmark 对应关系。
7. 从私有 manifest 读取标准状态。
8. 比较模型分类和标准状态。
9. 分类错误或无法读取时，立即判错，不调用 cvc5。
10. 分类正确且为 SAT/UNSAT 时，才运行对应的证书验证器。
11. 分别记录分类正确性和证书有效性。

流程可以概括为：

```text
无标签输入 -> 模型回答 -> 比较分类
                           ├─ 分类错误：停止，fully_solved=false
                           └─ 分类正确：使用 cvc5 验证证书
                                        ├─ 证书无效：fully_solved=false
                                        └─ 证书有效：fully_solved=true
```

### SAT 证书验证

验证器执行以下检查：

1. 每个原始零参数符号必须在 `constants` 中恰好出现一次。
2. 每个原始正参数函数必须在 `functions` 中恰好出现一次。
3. sort、参数类型和返回类型必须与原始声明完全一致。
4. 每个 `value_smt2` 和 `body_smt2` 必须恰好是一个 SMT-LIB term。
5. 拒绝命令注入、缺少符号、额外符号、重复符号、不安全 binder 和证书中的循环符号引用。
6. 为常量生成等式约束，为函数生成全称量化解释约束。
7. 将证书约束与原始 SMT-LIB 公式组合。
8. 只有固定版本 cvc5 返回 `sat` 且退出码为 0 时才接受。

只有输入本身没有零参数声明时，`constants=[]` 才是完整证书；它不能用于省略本应赋值的变量。

### UNSAT 证书验证

验证器执行以下步骤：

1. 在不破坏理论原子边界的情况下解析外层 CNF。
2. 检查子句编号为唯一、正数且从 1 开始。
3. 只重建模型选择的子句。
4. 声明其中使用的 Tseitin 布尔辅助变量。
5. 递归展开 `lambda` 定义辅助项。
6. 拒绝格式错误、冲突、循环定义或过大的重建公式。
7. 只有固定版本 cvc5 返回 `unsat` 且退出码为 0 时才接受。

当前 UNSAT 证书是不可满足核心，仍由 cvc5 完成最终理论证明，不等同于独立形式化证明。后续可以增加 Alethe 或 LRAT 作为更强的证明实验。

## 评分字段

每次有效模型响应至少记录：

```json
{
  "prediction": "sat",
  "expected": "sat",
  "verdict_correct": true,
  "certificate_present": true,
  "certificate_checked": true,
  "certificate_valid": true,
  "certificate_skip_reason": null,
  "fully_solved": true
}
```

只有 `verdict_correct` 和 `certificate_valid` 同时为真时，`fully_solved` 才为真。最终需要分别对“分类正确”和“完整求解”统计每题每模型的 5/5、4/5、3/5、2/5、1/5、0/5 分布，不能用多数投票覆盖单次结果。

## 实验目录和产物

每次实验独立存放在：

```text
experiments/<模型>/runs/<UTC时间戳>__<实验内容>__<配置>/
```

主要文件包括：

- `configuration.json`：本次不可变配置快照；
- `prompt.txt`：本次 prompt 快照；
- `raw/`：模型最终回答和 reasoning 数据；
- `logs/`：Token、耗时、finish reason 和错误；
- `verifier/`：根据证书生成并交给 cvc5 的 SMT-LIB；
- `results/runs.jsonl`：每次模型响应的评分记录；
- `results/infrastructure-errors.jsonl`：可重试的基础设施错误；
- `results/summary.json`：完成后的汇总；
- `full-run.stdout.log`、`full-run.stderr.log`：实时运行日志；
- `launcher.json`：后台 PID 和实验目录信息。

DeepSeek 保存 API 明确返回的 `reasoning_content`。Codex 保存完整 CLI JSONL 事件流和 CLI 明确返回的 reasoning summary。隐藏思维链不会由接口提供，本项目不会伪造或反推隐藏思维链。

## 运行命令

单独验证一个证书：

```powershell
python experiments/certificate-verifier/scripts/verify_certificate.py `
  --case benchmarks/certificate-inputs/cases/LIA/case-....json `
  --response response.json
```

运行或继续 Flash：

```powershell
python experiments/deepseek-v4-flash/scripts/run_certificate.py `
  --run-directory RUN_NAME --workers 4 --max-tokens 32768

python experiments/deepseek-v4-flash/scripts/run_certificate.py `
  --run-directory RUN_NAME --workers 4 --max-tokens 32768 --resume
```

运行 Pro：

```powershell
python experiments/deepseek-v4-pro/scripts/run_certificate.py `
  --run-directory RUN_NAME --workers 4 --max-tokens 32768
```

运行或继续 Codex：

```powershell
python experiments/codex-gpt-5.6-sol/scripts/run_codex.py `
  --run-directory RUN_NAME --experiment-id cnf-certificate-full-v1

python experiments/codex-gpt-5.6-sol/scripts/run_codex.py `
  --run-directory RUN_NAME --experiment-id cnf-certificate-full-v1 --resume
```

付费全量实验前应先使用 `--dry-run`。运行产物和项目根目录的 `api-key` 已由 Git 忽略。

## 可信验证器

项目固定使用 `tools/cvc5/` 下的 cvc5 1.3.3。模型回答完成前不得使用 cvc5；它只在分类正确后充当证书裁判。验证器通过参数数组在隔离临时目录中调用 cvc5，模型输出始终只作为数据解析，绝不会作为 Python、PowerShell 或其他程序执行。
