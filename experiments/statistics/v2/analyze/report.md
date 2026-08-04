# v2 实验分析报告

> 本报告基于完整的 93 个测试用例 × 3 个模型 × 5 次重复实验。最终成功定义为：正确 UNSAT，或正确 SAT 且模型 witness 通过 cvc5。SAT/UNSAT Accuracy 只看分类；SAT witness rate 只在分类正确的 SAT 回答中计算。

## 1. 实验范围与总体结果

- 批次状态：`complete`；每模型 93 题、465 次。
- 排除用例：`QF_ALIA/case-875434a9d4afb78d0f4f.json`, `QF_NIRA/case-6424ad354fc044b5c06c.json`（统一对三个模型排除）。

| 模型 | 完成 | SAT/UNSAT 正确 | Accuracy | 有效 SAT witness | 正确 SAT | Witness rate | 正确 UNSAT |
|---|---:|---:|---:|---:|---:|---:|---:|
| Codex 5.6 Sol | 465/465 | 449/465 | 96.56% | 173 | 214 | 80.84% | 235 |
| DeepSeek V4 Flash | 465/465 | 403/465 | 86.67% | 139 | 189 | 73.54% | 214 |
| DeepSeek V4 Pro | 465/465 | 356/465 | 76.56% | 105 | 165 | 63.64% | 191 |

### 最终成功次数分布

| 模型 | 5/5 | 4/5 | 3/5 | 2/5 | 1/5 | 0/5 |
|---|---:|---:|---:|---:|---:|---:|
| Codex 5.6 Sol | 73 | 7 | 5 | 0 | 0 | 8 |
| DeepSeek V4 Flash | 52 | 17 | 6 | 3 | 1 | 14 |
| DeepSeek V4 Pro | 43 | 13 | 3 | 7 | 6 | 21 |

### 按逻辑的指标

| 模型 | 逻辑 | Accuracy | SAT witness rate |
|---|---|---:|---:|
| Codex 5.6 Sol | ABVFP | 100.00% | 100.00% |
| Codex 5.6 Sol | ALIA | 95.00% | 100.00% |
| Codex 5.6 Sol | LIA | 96.67% | 50.00% |
| Codex 5.6 Sol | NIA | 98.33% | 100.00% |
| Codex 5.6 Sol | NRA | 100.00% | 80.00% |
| Codex 5.6 Sol | QF_ALIA | 85.45% | 90.91% |
| Codex 5.6 Sol | QF_AUFLIA | 96.67% | 33.33% |
| Codex 5.6 Sol | QF_NIRA | 100.00% | — |
| Codex 5.6 Sol | QF_S | 100.00% | 100.00% |
| DeepSeek V4 Flash | ABVFP | 100.00% | 84.44% |
| DeepSeek V4 Flash | ALIA | 85.00% | 100.00% |
| DeepSeek V4 Flash | LIA | 85.00% | 44.00% |
| DeepSeek V4 Flash | NIA | 90.00% | 96.55% |
| DeepSeek V4 Flash | NRA | 100.00% | 76.00% |
| DeepSeek V4 Flash | QF_ALIA | 50.91% | 100.00% |
| DeepSeek V4 Flash | QF_AUFLIA | 83.33% | 35.71% |
| DeepSeek V4 Flash | QF_NIRA | 100.00% | — |
| DeepSeek V4 Flash | QF_S | 98.33% | 86.21% |
| DeepSeek V4 Pro | ABVFP | 93.33% | 45.24% |
| DeepSeek V4 Pro | ALIA | 61.67% | 80.00% |
| DeepSeek V4 Pro | LIA | 80.00% | 40.91% |
| DeepSeek V4 Pro | NIA | 78.33% | 88.00% |
| DeepSeek V4 Pro | NRA | 98.33% | 76.00% |
| DeepSeek V4 Pro | QF_ALIA | 38.18% | — |
| DeepSeek V4 Pro | QF_AUFLIA | 75.00% | 42.86% |
| DeepSeek V4 Pro | QF_NIRA | 100.00% | — |
| DeepSeek V4 Pro | QF_S | 86.67% | 92.00% |

## 2. 各模型 0/5～5/5 用例汇总

下列分桶依据最终成功，而不是只看 SAT/UNSAT 分类。每项格式为 `逻辑/文件名 [golden, clauses, CNF字符数]`。

### Codex 5.6 Sol

#### 5/5（73 题）

- `ABVFP/308e5a972a-double_req_bl_0320_true-unreach-call.c_4.md` [sat, 15 clauses, 1782 chars]
- `ABVFP/302cf07a5e-float_req_bl_0530b_true-unreach-call.c_5.md` [sat, 12 clauses, 14637 chars]
- `ABVFP/dd5e3b0351-float_req_bl_1210_false-unreach-call.c_0.md` [sat, 6 clauses, 1234 chars]
- `ABVFP/189893bdbb-float_req_bl_0530b_true-unreach-call.c_2.md` [sat, 13 clauses, 15505 chars]
- `ABVFP/a2be3080e2-float_req_bl_0621b_true-unreach-call.c_1.md` [sat, 11 clauses, 11093 chars]
- `ABVFP/ac2811a735-float_req_bl_0684a_true-unreach-call.c_4.md` [sat, 11 clauses, 11093 chars]
- `ABVFP/0c12618c85-float_req_bl_0682a_true-unreach-call.c_13.md` [sat, 14 clauses, 2832 chars]
- `ABVFP/ea7e47b81e-float_req_bl_0620b_true-unreach-call.c_6.md` [sat, 12 clauses, 11792 chars]
- `ABVFP/ea681cac71-float_req_bl_0530b_true-unreach-call.c_8.md` [sat, 13 clauses, 15284 chars]
- `ALIA/57ada40aa8-piVC_098a89.md` [unsat, 115 clauses, 7509 chars]
- `ALIA/5ed037e3cc-piVC_ffb7db.md` [unsat, 190 clauses, 8871 chars]
- `ALIA/af7d7d155d-piVC_7f6962.md` [unsat, 46 clauses, 1947 chars]
- `ALIA/af81486a3f-piVC_c5a79f.md` [unsat, 37 clauses, 1462 chars]
- `ALIA/e46b638c7c-piVC_982830.sat.md` [sat, 10 clauses, 968 chars]
- `ALIA/dba123416f-piVC_600bf6.md` [unsat, 13 clauses, 563 chars]
- `ALIA/cce1e61ff2-piVC_3240b6.md` [unsat, 61 clauses, 3525 chars]
- `ALIA/dd3cff8a69-piVC_5cee0c.md` [unsat, 172 clauses, 10147 chars]
- `ALIA/4c97df26e7-piVC_bd0142.md` [unsat, 172 clauses, 10149 chars]
- `ALIA/bdd5eb546d-piVC_a04477.md` [unsat, 190 clauses, 8869 chars]
- `LIA/818325b2de-nested9_true-unreach-call.i_1749.md` [unsat, 13 clauses, 1046 chars]
- `LIA/ee94632839-138.md` [unsat, 36 clauses, 181634 chars]
- `LIA/514835a5aa-jain_7_true-unreach-call_true-no-overflow_false-termination.i_5.md` [unsat, 10 clauses, 2361 chars]
- `LIA/86ece07d34-ARI011=1.md` [unsat, 1 clauses, 34 chars]
- `LIA/0afccb8013-009.md` [sat, 21 clauses, 6733 chars]
- `LIA/4d472d34fe-NUM874=1.md` [sat, 1 clauses, 42 chars]
- `LIA/7e33141df7-nested9_true-unreach-call.i_1676.md` [unsat, 15 clauses, 1224 chars]
- `LIA/87f585dce5-nested9_true-unreach-call.i_670.md` [unsat, 13 clauses, 816 chars]
- `NIA/6097397d24-Problem17_label54_false-unreach-call.c_10.md` [sat, 23 clauses, 5397 chars]
- `NIA/d2baf9a6e3-184.md` [unsat, 14 clauses, 30570 chars]
- `NIA/adba4fcc0d-Problem17_label54_false-unreach-call.c_12.md` [sat, 25 clauses, 1367 chars]
- `NIA/520443d627-183.md` [sat, 9 clauses, 30442 chars]
- `NIA/d8e2e6a94b-byte_add_1_true-unreach-call_true-no-overflow_true-termination.i_1.md` [sat, 6 clauses, 373 chars]
- `NIA/f78bd5b9f4-NUM878=1.md` [unsat, 1 clauses, 42 chars]
- `NIA/b9297b0cc3-ARI123=1.md` [unsat, 1 clauses, 180 chars]
- `NIA/33b3fa2910-jain_6_true-unreach-call_true-no-overflow_false-termination.i_0.md` [unsat, 11 clauses, 890 chars]
- `NIA/63da306c9c-Problem18_label34_false-unreach-call.c_13.md` [unsat, 2 clauses, 701 chars]
- `NIA/41a6c07a20-jain_6_true-unreach-call_true-no-overflow_false-termination.i_11.md` [unsat, 11 clauses, 1549 chars]
- `NIA/11d889a116-NUM885=1.md` [sat, 1 clauses, 42 chars]
- `NRA/05f6f3c412-intersection-example-simple.proof-node139846.md` [unsat, 1 clauses, 1003 chars]
- `NRA/5de9b96fd7-strassen-trivial.md` [sat, 1 clauses, 3069 chars]
- `NRA/b71c706c27-ETCS-essentials-live-range2.proof-node1046.md` [sat, 1 clauses, 807 chars]
- `NRA/3f4c9f1d1c-strassen-linear.md` [sat, 1 clauses, 3492 chars]
- `NRA/7af8bd92ec-intersection-example-simple.proof-node123456.md` [unsat, 1 clauses, 827 chars]
- `NRA/b8c28b67ab-intersection-example-simple.proof-node469037.md` [unsat, 1 clauses, 877 chars]
- `NRA/f73795ffcb-strassen-impossible.md` [unsat, 1 clauses, 4992 chars]
- `NRA/18dc573cc5-intersection-example-simple.proof-node256483.md` [unsat, 1 clauses, 852 chars]
- `NRA/a94c71fdd6-reactivity-lemma-node2938.md` [sat, 1 clauses, 606 chars]
- `NRA/6a99aa37dd-intersection-example-simple.proof-node729267.md` [unsat, 1 clauses, 1248 chars]
- `NRA/f93694880b-moving-point-node2370.md` [unsat, 1 clauses, 468 chars]
- `QF_ALIA/679e0ffaa9-ios_t1_ios_bia_np_sf_ai_00001_001.cvc.md` [unsat, 10 clauses, 247 chars]
- `QF_ALIA/faf9ed7349-qlock.base.13.md` [unsat, 1792 clauses, 52515 chars]
- `QF_ALIA/c440748714-ios_t1_ios_np_sf_ai_00005_001.cvc.md` [unsat, 29 clauses, 1086 chars]
- `QF_ALIA/20d5cd5790-ios_t1_ios_bia_np_sf_ai_00013_001.cvc.md` [unsat, 70 clauses, 2055 chars]
- `QF_ALIA/6f593bfcf9-piVC_ed9849.md` [unsat, 1597 clauses, 63276 chars]
- `QF_AUFLIA/55ac8ba8a7-smt6416286979991758948.md` [sat, 1 clauses, 32 chars]
- `QF_AUFLIA/5a4e2f93cf-smt3150137541310906277.md` [unsat, 1 clauses, 35 chars]
- `QF_AUFLIA/a4c8726cf4-swap_t3_pp_sf_ai_00010_001.cvc.md` [unsat, 82 clauses, 3171 chars]
- `QF_AUFLIA/4f8b0ac98d-swap_t1_pp_nf_ai_00006_004.cvc.md` [unsat, 1 clauses, 113623 chars]
- `QF_AUFLIA/e0c208863b-storecomm_invalid_t1_np_nf_ni_00020_006.cvc.md` [sat, 1 clauses, 577 chars]
- `QF_AUFLIA/04508b93b7-storecomm_t1_pp_nf_ni_00040_006.cvc.md` [unsat, 1 clauses, 3547 chars]
- `QF_NIRA/31712594c2-test_union_cast-1_true-unreach-call.i.md` [unsat, 22 clauses, 1086 chars]
- `QF_S/331f17148e-instance07316.md` [unsat, 5 clauses, 21826 chars]
- `QF_S/abaf4d3d22-benchmark_0059.md` [unsat, 7 clauses, 434 chars]
- `QF_S/fae5a3418c-instance12239.md` [sat, 3 clauses, 1011 chars]
- `QF_S/1783153d73-instance01388.md` [sat, 1 clauses, 148 chars]
- `QF_S/a079644c39-instance09604.md` [sat, 3 clauses, 20723 chars]
- `QF_S/742c644e56-instance07485.md` [unsat, 5 clauses, 1846 chars]
- `QF_S/a9ab9a5064-01_track_83.md` [sat, 1 clauses, 41 chars]
- `QF_S/cf25ee2a87-parikh.md` [unsat, 1 clauses, 46 chars]
- `QF_S/bd772f7bb3-instance13944.md` [unsat, 5 clauses, 1159 chars]
- `QF_S/561b5c6a36-instance12664.md` [sat, 2 clauses, 290 chars]
- `QF_S/e1dffe5729-instance06765.md` [unsat, 3 clauses, 786 chars]
- `QF_S/1ac968b76c-benchmark_0286.md` [sat, 7 clauses, 434 chars]

#### 4/5（7 题）

- `ALIA/f6285a256e-piVC_849b63.md` [unsat, 169 clauses, 10033 chars]
- `LIA/07d23f440c-076.md` [sat, 63 clauses, 60282 chars]
- `NIA/2da4538e94-Problem17_label54_false-unreach-call.c_13.md` [sat, 13 clauses, 971 chars]
- `QF_ALIA/76fabb1637-stack-invalid-6.md` [sat, 265 clauses, 10763 chars]
- `QF_ALIA/60d1a1277d-qlock.induction.25.md` [sat, 3388 clauses, 101232 chars]
- `QF_AUFLIA/a6831a3fb1-pp-TakenBranch-s2e.md` [unsat, 2264 clauses, 130285 chars]
- `QF_AUFLIA/d9b30f8346-smt5720223571793459860.md` [unsat, 13 clauses, 440 chars]

#### 3/5（5 题）

- `ALIA/499ffa55ba-piVC_2186b5.md` [unsat, 166 clauses, 9961 chars]
- `QF_ALIA/b1092fb93e-qlock.base.30.md` [sat, 4087 clauses, 123893 chars]
- `QF_ALIA/28114b6375-qlock-bug2-10.md` [sat, 1387 clauses, 40219 chars]
- `QF_ALIA/96eb0f0ccb-qlock.base.20.md` [sat, 2737 clauses, 81159 chars]
- `QF_ALIA/d6617f16d8-qlock.induction.16.md` [sat, 2173 clauses, 63909 chars]

#### 2/5（0 题）

无。

#### 1/5（0 题）

无。

#### 0/5（8 题）

- `LIA/a60b6e08c6-fcp_197_199.md` [sat, 5 clauses, 539 chars]
- `LIA/01b211cc37-fcp_167_173_179.md` [sat, 5 clauses, 659 chars]
- `LIA/4935b59fa2-137.md` [sat, 32 clauses, 181553 chars]
- `NRA/722eaea277-strassen-hard.md` [sat, 1 clauses, 5052 chars]
- `QF_AUFLIA/41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md` [sat, 24 clauses, 775 chars]
- `QF_AUFLIA/088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md` [sat, 1894 clauses, 37992 chars]
- `QF_AUFLIA/e387ddf96f-storecomm_invalid_t1_pp_sf_ai_00020_001.cvc.md` [sat, 234 clauses, 5043 chars]
- `QF_AUFLIA/3d0fe3ca5c-swap_invalid_t3_pp_sf_ai_00006_004.cvc.md` [sat, 47 clauses, 1698 chars]

### DeepSeek V4 Flash

#### 5/5（52 题）

- `ABVFP/308e5a972a-double_req_bl_0320_true-unreach-call.c_4.md` [sat, 15 clauses, 1782 chars]
- `ABVFP/302cf07a5e-float_req_bl_0530b_true-unreach-call.c_5.md` [sat, 12 clauses, 14637 chars]
- `ABVFP/a2be3080e2-float_req_bl_0621b_true-unreach-call.c_1.md` [sat, 11 clauses, 11093 chars]
- `ABVFP/ac2811a735-float_req_bl_0684a_true-unreach-call.c_4.md` [sat, 11 clauses, 11093 chars]
- `ALIA/57ada40aa8-piVC_098a89.md` [unsat, 115 clauses, 7509 chars]
- `ALIA/af7d7d155d-piVC_7f6962.md` [unsat, 46 clauses, 1947 chars]
- `ALIA/e46b638c7c-piVC_982830.sat.md` [sat, 10 clauses, 968 chars]
- `ALIA/dba123416f-piVC_600bf6.md` [unsat, 13 clauses, 563 chars]
- `ALIA/cce1e61ff2-piVC_3240b6.md` [unsat, 61 clauses, 3525 chars]
- `LIA/514835a5aa-jain_7_true-unreach-call_true-no-overflow_false-termination.i_5.md` [unsat, 10 clauses, 2361 chars]
- `LIA/86ece07d34-ARI011=1.md` [unsat, 1 clauses, 34 chars]
- `LIA/4d472d34fe-NUM874=1.md` [sat, 1 clauses, 42 chars]
- `LIA/7e33141df7-nested9_true-unreach-call.i_1676.md` [unsat, 15 clauses, 1224 chars]
- `LIA/87f585dce5-nested9_true-unreach-call.i_670.md` [unsat, 13 clauses, 816 chars]
- `NIA/adba4fcc0d-Problem17_label54_false-unreach-call.c_12.md` [sat, 25 clauses, 1367 chars]
- `NIA/d8e2e6a94b-byte_add_1_true-unreach-call_true-no-overflow_true-termination.i_1.md` [sat, 6 clauses, 373 chars]
- `NIA/f78bd5b9f4-NUM878=1.md` [unsat, 1 clauses, 42 chars]
- `NIA/b9297b0cc3-ARI123=1.md` [unsat, 1 clauses, 180 chars]
- `NIA/33b3fa2910-jain_6_true-unreach-call_true-no-overflow_false-termination.i_0.md` [unsat, 11 clauses, 890 chars]
- `NIA/63da306c9c-Problem18_label34_false-unreach-call.c_13.md` [unsat, 2 clauses, 701 chars]
- `NIA/41a6c07a20-jain_6_true-unreach-call_true-no-overflow_false-termination.i_11.md` [unsat, 11 clauses, 1549 chars]
- `NIA/11d889a116-NUM885=1.md` [sat, 1 clauses, 42 chars]
- `NIA/2da4538e94-Problem17_label54_false-unreach-call.c_13.md` [sat, 13 clauses, 971 chars]
- `NRA/05f6f3c412-intersection-example-simple.proof-node139846.md` [unsat, 1 clauses, 1003 chars]
- `NRA/5de9b96fd7-strassen-trivial.md` [sat, 1 clauses, 3069 chars]
- `NRA/b71c706c27-ETCS-essentials-live-range2.proof-node1046.md` [sat, 1 clauses, 807 chars]
- `NRA/3f4c9f1d1c-strassen-linear.md` [sat, 1 clauses, 3492 chars]
- `NRA/7af8bd92ec-intersection-example-simple.proof-node123456.md` [unsat, 1 clauses, 827 chars]
- `NRA/b8c28b67ab-intersection-example-simple.proof-node469037.md` [unsat, 1 clauses, 877 chars]
- `NRA/f73795ffcb-strassen-impossible.md` [unsat, 1 clauses, 4992 chars]
- `NRA/18dc573cc5-intersection-example-simple.proof-node256483.md` [unsat, 1 clauses, 852 chars]
- `NRA/6a99aa37dd-intersection-example-simple.proof-node729267.md` [unsat, 1 clauses, 1248 chars]
- `NRA/f93694880b-moving-point-node2370.md` [unsat, 1 clauses, 468 chars]
- `QF_ALIA/679e0ffaa9-ios_t1_ios_bia_np_sf_ai_00001_001.cvc.md` [unsat, 10 clauses, 247 chars]
- `QF_ALIA/faf9ed7349-qlock.base.13.md` [unsat, 1792 clauses, 52515 chars]
- `QF_ALIA/c440748714-ios_t1_ios_np_sf_ai_00005_001.cvc.md` [unsat, 29 clauses, 1086 chars]
- `QF_ALIA/20d5cd5790-ios_t1_ios_bia_np_sf_ai_00013_001.cvc.md` [unsat, 70 clauses, 2055 chars]
- `QF_ALIA/6f593bfcf9-piVC_ed9849.md` [unsat, 1597 clauses, 63276 chars]
- `QF_AUFLIA/55ac8ba8a7-smt6416286979991758948.md` [sat, 1 clauses, 32 chars]
- `QF_AUFLIA/5a4e2f93cf-smt3150137541310906277.md` [unsat, 1 clauses, 35 chars]
- `QF_AUFLIA/d9b30f8346-smt5720223571793459860.md` [unsat, 13 clauses, 440 chars]
- `QF_AUFLIA/e0c208863b-storecomm_invalid_t1_np_nf_ni_00020_006.cvc.md` [sat, 1 clauses, 577 chars]
- `QF_AUFLIA/04508b93b7-storecomm_t1_pp_nf_ni_00040_006.cvc.md` [unsat, 1 clauses, 3547 chars]
- `QF_NIRA/31712594c2-test_union_cast-1_true-unreach-call.i.md` [unsat, 22 clauses, 1086 chars]
- `QF_S/331f17148e-instance07316.md` [unsat, 5 clauses, 21826 chars]
- `QF_S/abaf4d3d22-benchmark_0059.md` [unsat, 7 clauses, 434 chars]
- `QF_S/a079644c39-instance09604.md` [sat, 3 clauses, 20723 chars]
- `QF_S/742c644e56-instance07485.md` [unsat, 5 clauses, 1846 chars]
- `QF_S/a9ab9a5064-01_track_83.md` [sat, 1 clauses, 41 chars]
- `QF_S/cf25ee2a87-parikh.md` [unsat, 1 clauses, 46 chars]
- `QF_S/bd772f7bb3-instance13944.md` [unsat, 5 clauses, 1159 chars]
- `QF_S/e1dffe5729-instance06765.md` [unsat, 3 clauses, 786 chars]

#### 4/5（17 题）

- `ABVFP/dd5e3b0351-float_req_bl_1210_false-unreach-call.c_0.md` [sat, 6 clauses, 1234 chars]
- `ABVFP/0c12618c85-float_req_bl_0682a_true-unreach-call.c_13.md` [sat, 14 clauses, 2832 chars]
- `ABVFP/ea7e47b81e-float_req_bl_0620b_true-unreach-call.c_6.md` [sat, 12 clauses, 11792 chars]
- `ALIA/5ed037e3cc-piVC_ffb7db.md` [unsat, 190 clauses, 8871 chars]
- `ALIA/499ffa55ba-piVC_2186b5.md` [unsat, 166 clauses, 9961 chars]
- `ALIA/af81486a3f-piVC_c5a79f.md` [unsat, 37 clauses, 1462 chars]
- `ALIA/dd3cff8a69-piVC_5cee0c.md` [unsat, 172 clauses, 10147 chars]
- `ALIA/bdd5eb546d-piVC_a04477.md` [unsat, 190 clauses, 8869 chars]
- `LIA/818325b2de-nested9_true-unreach-call.i_1749.md` [unsat, 13 clauses, 1046 chars]
- `LIA/0afccb8013-009.md` [sat, 21 clauses, 6733 chars]
- `NIA/6097397d24-Problem17_label54_false-unreach-call.c_10.md` [sat, 23 clauses, 5397 chars]
- `NIA/520443d627-183.md` [sat, 9 clauses, 30442 chars]
- `NRA/a94c71fdd6-reactivity-lemma-node2938.md` [sat, 1 clauses, 606 chars]
- `QF_AUFLIA/a4c8726cf4-swap_t3_pp_sf_ai_00010_001.cvc.md` [unsat, 82 clauses, 3171 chars]
- `QF_S/fae5a3418c-instance12239.md` [sat, 3 clauses, 1011 chars]
- `QF_S/1783153d73-instance01388.md` [sat, 1 clauses, 148 chars]
- `QF_S/561b5c6a36-instance12664.md` [sat, 2 clauses, 290 chars]

#### 3/5（6 题）

- `ABVFP/189893bdbb-float_req_bl_0530b_true-unreach-call.c_2.md` [sat, 13 clauses, 15505 chars]
- `ABVFP/ea681cac71-float_req_bl_0530b_true-unreach-call.c_8.md` [sat, 13 clauses, 15284 chars]
- `ALIA/f6285a256e-piVC_849b63.md` [unsat, 169 clauses, 10033 chars]
- `ALIA/4c97df26e7-piVC_bd0142.md` [unsat, 172 clauses, 10149 chars]
- `QF_ALIA/76fabb1637-stack-invalid-6.md` [sat, 265 clauses, 10763 chars]
- `QF_S/1ac968b76c-benchmark_0286.md` [sat, 7 clauses, 434 chars]

#### 2/5（3 题）

- `LIA/ee94632839-138.md` [unsat, 36 clauses, 181634 chars]
- `LIA/07d23f440c-076.md` [sat, 63 clauses, 60282 chars]
- `QF_AUFLIA/4f8b0ac98d-swap_t1_pp_nf_ai_00006_004.cvc.md` [unsat, 1 clauses, 113623 chars]

#### 1/5（1 题）

- `QF_AUFLIA/a6831a3fb1-pp-TakenBranch-s2e.md` [unsat, 2264 clauses, 130285 chars]

#### 0/5（14 题）

- `LIA/a60b6e08c6-fcp_197_199.md` [sat, 5 clauses, 539 chars]
- `LIA/01b211cc37-fcp_167_173_179.md` [sat, 5 clauses, 659 chars]
- `LIA/4935b59fa2-137.md` [sat, 32 clauses, 181553 chars]
- `NIA/d2baf9a6e3-184.md` [unsat, 14 clauses, 30570 chars]
- `NRA/722eaea277-strassen-hard.md` [sat, 1 clauses, 5052 chars]
- `QF_ALIA/b1092fb93e-qlock.base.30.md` [sat, 4087 clauses, 123893 chars]
- `QF_ALIA/28114b6375-qlock-bug2-10.md` [sat, 1387 clauses, 40219 chars]
- `QF_ALIA/60d1a1277d-qlock.induction.25.md` [sat, 3388 clauses, 101232 chars]
- `QF_ALIA/96eb0f0ccb-qlock.base.20.md` [sat, 2737 clauses, 81159 chars]
- `QF_ALIA/d6617f16d8-qlock.induction.16.md` [sat, 2173 clauses, 63909 chars]
- `QF_AUFLIA/41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md` [sat, 24 clauses, 775 chars]
- `QF_AUFLIA/088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md` [sat, 1894 clauses, 37992 chars]
- `QF_AUFLIA/e387ddf96f-storecomm_invalid_t1_pp_sf_ai_00020_001.cvc.md` [sat, 234 clauses, 5043 chars]
- `QF_AUFLIA/3d0fe3ca5c-swap_invalid_t3_pp_sf_ai_00006_004.cvc.md` [sat, 47 clauses, 1698 chars]

### DeepSeek V4 Pro

#### 5/5（43 题）

- `ALIA/af7d7d155d-piVC_7f6962.md` [unsat, 46 clauses, 1947 chars]
- `ALIA/af81486a3f-piVC_c5a79f.md` [unsat, 37 clauses, 1462 chars]
- `ALIA/dba123416f-piVC_600bf6.md` [unsat, 13 clauses, 563 chars]
- `ALIA/cce1e61ff2-piVC_3240b6.md` [unsat, 61 clauses, 3525 chars]
- `LIA/818325b2de-nested9_true-unreach-call.i_1749.md` [unsat, 13 clauses, 1046 chars]
- `LIA/514835a5aa-jain_7_true-unreach-call_true-no-overflow_false-termination.i_5.md` [unsat, 10 clauses, 2361 chars]
- `LIA/86ece07d34-ARI011=1.md` [unsat, 1 clauses, 34 chars]
- `LIA/4d472d34fe-NUM874=1.md` [sat, 1 clauses, 42 chars]
- `LIA/7e33141df7-nested9_true-unreach-call.i_1676.md` [unsat, 15 clauses, 1224 chars]
- `LIA/87f585dce5-nested9_true-unreach-call.i_670.md` [unsat, 13 clauses, 816 chars]
- `NIA/d8e2e6a94b-byte_add_1_true-unreach-call_true-no-overflow_true-termination.i_1.md` [sat, 6 clauses, 373 chars]
- `NIA/f78bd5b9f4-NUM878=1.md` [unsat, 1 clauses, 42 chars]
- `NIA/b9297b0cc3-ARI123=1.md` [unsat, 1 clauses, 180 chars]
- `NIA/33b3fa2910-jain_6_true-unreach-call_true-no-overflow_false-termination.i_0.md` [unsat, 11 clauses, 890 chars]
- `NIA/41a6c07a20-jain_6_true-unreach-call_true-no-overflow_false-termination.i_11.md` [unsat, 11 clauses, 1549 chars]
- `NIA/11d889a116-NUM885=1.md` [sat, 1 clauses, 42 chars]
- `NIA/2da4538e94-Problem17_label54_false-unreach-call.c_13.md` [sat, 13 clauses, 971 chars]
- `NRA/05f6f3c412-intersection-example-simple.proof-node139846.md` [unsat, 1 clauses, 1003 chars]
- `NRA/5de9b96fd7-strassen-trivial.md` [sat, 1 clauses, 3069 chars]
- `NRA/b71c706c27-ETCS-essentials-live-range2.proof-node1046.md` [sat, 1 clauses, 807 chars]
- `NRA/7af8bd92ec-intersection-example-simple.proof-node123456.md` [unsat, 1 clauses, 827 chars]
- `NRA/b8c28b67ab-intersection-example-simple.proof-node469037.md` [unsat, 1 clauses, 877 chars]
- `NRA/f73795ffcb-strassen-impossible.md` [unsat, 1 clauses, 4992 chars]
- `NRA/a94c71fdd6-reactivity-lemma-node2938.md` [sat, 1 clauses, 606 chars]
- `NRA/6a99aa37dd-intersection-example-simple.proof-node729267.md` [unsat, 1 clauses, 1248 chars]
- `NRA/f93694880b-moving-point-node2370.md` [unsat, 1 clauses, 468 chars]
- `QF_ALIA/679e0ffaa9-ios_t1_ios_bia_np_sf_ai_00001_001.cvc.md` [unsat, 10 clauses, 247 chars]
- `QF_ALIA/c440748714-ios_t1_ios_np_sf_ai_00005_001.cvc.md` [unsat, 29 clauses, 1086 chars]
- `QF_ALIA/20d5cd5790-ios_t1_ios_bia_np_sf_ai_00013_001.cvc.md` [unsat, 70 clauses, 2055 chars]
- `QF_ALIA/6f593bfcf9-piVC_ed9849.md` [unsat, 1597 clauses, 63276 chars]
- `QF_AUFLIA/55ac8ba8a7-smt6416286979991758948.md` [sat, 1 clauses, 32 chars]
- `QF_AUFLIA/5a4e2f93cf-smt3150137541310906277.md` [unsat, 1 clauses, 35 chars]
- `QF_AUFLIA/d9b30f8346-smt5720223571793459860.md` [unsat, 13 clauses, 440 chars]
- `QF_AUFLIA/04508b93b7-storecomm_t1_pp_nf_ni_00040_006.cvc.md` [unsat, 1 clauses, 3547 chars]
- `QF_NIRA/31712594c2-test_union_cast-1_true-unreach-call.i.md` [unsat, 22 clauses, 1086 chars]
- `QF_S/331f17148e-instance07316.md` [unsat, 5 clauses, 21826 chars]
- `QF_S/fae5a3418c-instance12239.md` [sat, 3 clauses, 1011 chars]
- `QF_S/1783153d73-instance01388.md` [sat, 1 clauses, 148 chars]
- `QF_S/742c644e56-instance07485.md` [unsat, 5 clauses, 1846 chars]
- `QF_S/a9ab9a5064-01_track_83.md` [sat, 1 clauses, 41 chars]
- `QF_S/cf25ee2a87-parikh.md` [unsat, 1 clauses, 46 chars]
- `QF_S/bd772f7bb3-instance13944.md` [unsat, 5 clauses, 1159 chars]
- `QF_S/e1dffe5729-instance06765.md` [unsat, 3 clauses, 786 chars]

#### 4/5（13 题）

- `ABVFP/dd5e3b0351-float_req_bl_1210_false-unreach-call.c_0.md` [sat, 6 clauses, 1234 chars]
- `ABVFP/a2be3080e2-float_req_bl_0621b_true-unreach-call.c_1.md` [sat, 11 clauses, 11093 chars]
- `ABVFP/ea681cac71-float_req_bl_0530b_true-unreach-call.c_8.md` [sat, 13 clauses, 15284 chars]
- `ALIA/57ada40aa8-piVC_098a89.md` [unsat, 115 clauses, 7509 chars]
- `ALIA/e46b638c7c-piVC_982830.sat.md` [sat, 10 clauses, 968 chars]
- `LIA/0afccb8013-009.md` [sat, 21 clauses, 6733 chars]
- `NIA/adba4fcc0d-Problem17_label54_false-unreach-call.c_12.md` [sat, 25 clauses, 1367 chars]
- `NRA/3f4c9f1d1c-strassen-linear.md` [sat, 1 clauses, 3492 chars]
- `NRA/18dc573cc5-intersection-example-simple.proof-node256483.md` [unsat, 1 clauses, 852 chars]
- `QF_AUFLIA/4f8b0ac98d-swap_t1_pp_nf_ai_00006_004.cvc.md` [unsat, 1 clauses, 113623 chars]
- `QF_AUFLIA/e0c208863b-storecomm_invalid_t1_np_nf_ni_00020_006.cvc.md` [sat, 1 clauses, 577 chars]
- `QF_S/a079644c39-instance09604.md` [sat, 3 clauses, 20723 chars]
- `QF_S/561b5c6a36-instance12664.md` [sat, 2 clauses, 290 chars]

#### 3/5（3 题）

- `ABVFP/308e5a972a-double_req_bl_0320_true-unreach-call.c_4.md` [sat, 15 clauses, 1782 chars]
- `NIA/6097397d24-Problem17_label54_false-unreach-call.c_10.md` [sat, 23 clauses, 5397 chars]
- `QF_AUFLIA/a6831a3fb1-pp-TakenBranch-s2e.md` [unsat, 2264 clauses, 130285 chars]

#### 2/5（7 题）

- `ABVFP/ac2811a735-float_req_bl_0684a_true-unreach-call.c_4.md` [sat, 11 clauses, 11093 chars]
- `ALIA/5ed037e3cc-piVC_ffb7db.md` [unsat, 190 clauses, 8871 chars]
- `ALIA/dd3cff8a69-piVC_5cee0c.md` [unsat, 172 clauses, 10147 chars]
- `ALIA/4c97df26e7-piVC_bd0142.md` [unsat, 172 clauses, 10149 chars]
- `NIA/63da306c9c-Problem18_label34_false-unreach-call.c_13.md` [unsat, 2 clauses, 701 chars]
- `QF_AUFLIA/a4c8726cf4-swap_t3_pp_sf_ai_00010_001.cvc.md` [unsat, 82 clauses, 3171 chars]
- `QF_S/abaf4d3d22-benchmark_0059.md` [unsat, 7 clauses, 434 chars]

#### 1/5（6 题）

- `ABVFP/302cf07a5e-float_req_bl_0530b_true-unreach-call.c_5.md` [sat, 12 clauses, 14637 chars]
- `ABVFP/0c12618c85-float_req_bl_0682a_true-unreach-call.c_13.md` [sat, 14 clauses, 2832 chars]
- `ALIA/499ffa55ba-piVC_2186b5.md` [unsat, 166 clauses, 9961 chars]
- `ALIA/bdd5eb546d-piVC_a04477.md` [unsat, 190 clauses, 8869 chars]
- `LIA/ee94632839-138.md` [unsat, 36 clauses, 181634 chars]
- `QF_ALIA/faf9ed7349-qlock.base.13.md` [unsat, 1792 clauses, 52515 chars]

#### 0/5（21 题）

- `ABVFP/189893bdbb-float_req_bl_0530b_true-unreach-call.c_2.md` [sat, 13 clauses, 15505 chars]
- `ABVFP/ea7e47b81e-float_req_bl_0620b_true-unreach-call.c_6.md` [sat, 12 clauses, 11792 chars]
- `ALIA/f6285a256e-piVC_849b63.md` [unsat, 169 clauses, 10033 chars]
- `LIA/a60b6e08c6-fcp_197_199.md` [sat, 5 clauses, 539 chars]
- `LIA/01b211cc37-fcp_167_173_179.md` [sat, 5 clauses, 659 chars]
- `LIA/4935b59fa2-137.md` [sat, 32 clauses, 181553 chars]
- `LIA/07d23f440c-076.md` [sat, 63 clauses, 60282 chars]
- `NIA/d2baf9a6e3-184.md` [unsat, 14 clauses, 30570 chars]
- `NIA/520443d627-183.md` [sat, 9 clauses, 30442 chars]
- `NRA/722eaea277-strassen-hard.md` [sat, 1 clauses, 5052 chars]
- `QF_ALIA/b1092fb93e-qlock.base.30.md` [sat, 4087 clauses, 123893 chars]
- `QF_ALIA/28114b6375-qlock-bug2-10.md` [sat, 1387 clauses, 40219 chars]
- `QF_ALIA/76fabb1637-stack-invalid-6.md` [sat, 265 clauses, 10763 chars]
- `QF_ALIA/60d1a1277d-qlock.induction.25.md` [sat, 3388 clauses, 101232 chars]
- `QF_ALIA/96eb0f0ccb-qlock.base.20.md` [sat, 2737 clauses, 81159 chars]
- `QF_ALIA/d6617f16d8-qlock.induction.16.md` [sat, 2173 clauses, 63909 chars]
- `QF_AUFLIA/41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md` [sat, 24 clauses, 775 chars]
- `QF_AUFLIA/088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md` [sat, 1894 clauses, 37992 chars]
- `QF_AUFLIA/e387ddf96f-storecomm_invalid_t1_pp_sf_ai_00020_001.cvc.md` [sat, 234 clauses, 5043 chars]
- `QF_AUFLIA/3d0fe3ca5c-swap_invalid_t3_pp_sf_ai_00006_004.cvc.md` [sat, 47 clauses, 1698 chars]
- `QF_S/1ac968b76c-benchmark_0286.md` [sat, 7 clauses, 434 chars]

## 3. 三模型共同能力边界

- 三模型全部 15/15 成功：36 题。
- 三模型全部 0/15 成功：8 题。
- 其余题存在模型差异或重复运行波动；总成功次数越靠近 7～8/15，越接近当前模型族的经验能力边界。

### 共同稳定可解（15/15）

`ALIA/af7d7d155d-piVC_7f6962.md`, `ALIA/cce1e61ff2-piVC_3240b6.md`, `ALIA/dba123416f-piVC_600bf6.md`, `LIA/4d472d34fe-NUM874=1.md`, `LIA/514835a5aa-jain_7_true-unreach-call_true-no-overflow_false-termination.i_5.md`, `LIA/7e33141df7-nested9_true-unreach-call.i_1676.md`, `LIA/86ece07d34-ARI011=1.md`, `LIA/87f585dce5-nested9_true-unreach-call.i_670.md`, `NIA/11d889a116-NUM885=1.md`, `NIA/33b3fa2910-jain_6_true-unreach-call_true-no-overflow_false-termination.i_0.md`, `NIA/41a6c07a20-jain_6_true-unreach-call_true-no-overflow_false-termination.i_11.md`, `NIA/b9297b0cc3-ARI123=1.md`, `NIA/d8e2e6a94b-byte_add_1_true-unreach-call_true-no-overflow_true-termination.i_1.md`, `NIA/f78bd5b9f4-NUM878=1.md`, `NRA/05f6f3c412-intersection-example-simple.proof-node139846.md`, `NRA/5de9b96fd7-strassen-trivial.md`, `NRA/6a99aa37dd-intersection-example-simple.proof-node729267.md`, `NRA/7af8bd92ec-intersection-example-simple.proof-node123456.md`, `NRA/b71c706c27-ETCS-essentials-live-range2.proof-node1046.md`, `NRA/b8c28b67ab-intersection-example-simple.proof-node469037.md`, `NRA/f73795ffcb-strassen-impossible.md`, `NRA/f93694880b-moving-point-node2370.md`, `QF_ALIA/20d5cd5790-ios_t1_ios_bia_np_sf_ai_00013_001.cvc.md`, `QF_ALIA/679e0ffaa9-ios_t1_ios_bia_np_sf_ai_00001_001.cvc.md`, `QF_ALIA/6f593bfcf9-piVC_ed9849.md`, `QF_ALIA/c440748714-ios_t1_ios_np_sf_ai_00005_001.cvc.md`, `QF_AUFLIA/04508b93b7-storecomm_t1_pp_nf_ni_00040_006.cvc.md`, `QF_AUFLIA/55ac8ba8a7-smt6416286979991758948.md`, `QF_AUFLIA/5a4e2f93cf-smt3150137541310906277.md`, `QF_NIRA/31712594c2-test_union_cast-1_true-unreach-call.i.md`, `QF_S/331f17148e-instance07316.md`, `QF_S/742c644e56-instance07485.md`, `QF_S/a9ab9a5064-01_track_83.md`, `QF_S/bd772f7bb3-instance13944.md`, `QF_S/cf25ee2a87-parikh.md`, `QF_S/e1dffe5729-instance06765.md`

### 共同完全失败（0/15）

`LIA/01b211cc37-fcp_167_173_179.md`, `LIA/4935b59fa2-137.md`, `LIA/a60b6e08c6-fcp_197_199.md`, `NRA/722eaea277-strassen-hard.md`, `QF_AUFLIA/088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md`, `QF_AUFLIA/3d0fe3ca5c-swap_invalid_t3_pp_sf_ai_00006_004.cvc.md`, `QF_AUFLIA/41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md`, `QF_AUFLIA/e387ddf96f-storecomm_invalid_t1_pp_sf_ai_00020_001.cvc.md`

### 全部用例的跨模型总成功次数

| 总成功/15 | 题数 | 用例 |
|---:|---:|---|
| 15 | 36 | `ALIA/af7d7d155d-piVC_7f6962.md`, `ALIA/cce1e61ff2-piVC_3240b6.md`, `ALIA/dba123416f-piVC_600bf6.md`, `LIA/4d472d34fe-NUM874=1.md`, `LIA/514835a5aa-jain_7_true-unreach-call_true-no-overflow_false-termination.i_5.md`, `LIA/7e33141df7-nested9_true-unreach-call.i_1676.md`, `LIA/86ece07d34-ARI011=1.md`, `LIA/87f585dce5-nested9_true-unreach-call.i_670.md`, `NIA/11d889a116-NUM885=1.md`, `NIA/33b3fa2910-jain_6_true-unreach-call_true-no-overflow_false-termination.i_0.md`, `NIA/41a6c07a20-jain_6_true-unreach-call_true-no-overflow_false-termination.i_11.md`, `NIA/b9297b0cc3-ARI123=1.md`, `NIA/d8e2e6a94b-byte_add_1_true-unreach-call_true-no-overflow_true-termination.i_1.md`, `NIA/f78bd5b9f4-NUM878=1.md`, `NRA/05f6f3c412-intersection-example-simple.proof-node139846.md`, `NRA/5de9b96fd7-strassen-trivial.md`, `NRA/6a99aa37dd-intersection-example-simple.proof-node729267.md`, `NRA/7af8bd92ec-intersection-example-simple.proof-node123456.md`, `NRA/b71c706c27-ETCS-essentials-live-range2.proof-node1046.md`, `NRA/b8c28b67ab-intersection-example-simple.proof-node469037.md`, `NRA/f73795ffcb-strassen-impossible.md`, `NRA/f93694880b-moving-point-node2370.md`, `QF_ALIA/20d5cd5790-ios_t1_ios_bia_np_sf_ai_00013_001.cvc.md`, `QF_ALIA/679e0ffaa9-ios_t1_ios_bia_np_sf_ai_00001_001.cvc.md`, `QF_ALIA/6f593bfcf9-piVC_ed9849.md`, `QF_ALIA/c440748714-ios_t1_ios_np_sf_ai_00005_001.cvc.md`, `QF_AUFLIA/04508b93b7-storecomm_t1_pp_nf_ni_00040_006.cvc.md`, `QF_AUFLIA/55ac8ba8a7-smt6416286979991758948.md`, `QF_AUFLIA/5a4e2f93cf-smt3150137541310906277.md`, `QF_NIRA/31712594c2-test_union_cast-1_true-unreach-call.i.md`, `QF_S/331f17148e-instance07316.md`, `QF_S/742c644e56-instance07485.md`, `QF_S/a9ab9a5064-01_track_83.md`, `QF_S/bd772f7bb3-instance13944.md`, `QF_S/cf25ee2a87-parikh.md`, `QF_S/e1dffe5729-instance06765.md` |
| 14 | 15 | `ABVFP/a2be3080e2-float_req_bl_0621b_true-unreach-call.c_1.md`, `ALIA/57ada40aa8-piVC_098a89.md`, `ALIA/af81486a3f-piVC_c5a79f.md`, `ALIA/e46b638c7c-piVC_982830.sat.md`, `LIA/818325b2de-nested9_true-unreach-call.i_1749.md`, `NIA/2da4538e94-Problem17_label54_false-unreach-call.c_13.md`, `NIA/adba4fcc0d-Problem17_label54_false-unreach-call.c_12.md`, `NRA/18dc573cc5-intersection-example-simple.proof-node256483.md`, `NRA/3f4c9f1d1c-strassen-linear.md`, `NRA/a94c71fdd6-reactivity-lemma-node2938.md`, `QF_AUFLIA/d9b30f8346-smt5720223571793459860.md`, `QF_AUFLIA/e0c208863b-storecomm_invalid_t1_np_nf_ni_00020_006.cvc.md`, `QF_S/1783153d73-instance01388.md`, `QF_S/a079644c39-instance09604.md`, `QF_S/fae5a3418c-instance12239.md` |
| 13 | 4 | `ABVFP/308e5a972a-double_req_bl_0320_true-unreach-call.c_4.md`, `ABVFP/dd5e3b0351-float_req_bl_1210_false-unreach-call.c_0.md`, `LIA/0afccb8013-009.md`, `QF_S/561b5c6a36-instance12664.md` |
| 12 | 5 | `ABVFP/ac2811a735-float_req_bl_0684a_true-unreach-call.c_4.md`, `ABVFP/ea681cac71-float_req_bl_0530b_true-unreach-call.c_8.md`, `NIA/6097397d24-Problem17_label54_false-unreach-call.c_10.md`, `NIA/63da306c9c-Problem18_label34_false-unreach-call.c_13.md`, `QF_S/abaf4d3d22-benchmark_0059.md` |
| 11 | 6 | `ABVFP/302cf07a5e-float_req_bl_0530b_true-unreach-call.c_5.md`, `ALIA/5ed037e3cc-piVC_ffb7db.md`, `ALIA/dd3cff8a69-piVC_5cee0c.md`, `QF_ALIA/faf9ed7349-qlock.base.13.md`, `QF_AUFLIA/4f8b0ac98d-swap_t1_pp_nf_ai_00006_004.cvc.md`, `QF_AUFLIA/a4c8726cf4-swap_t3_pp_sf_ai_00010_001.cvc.md` |
| 10 | 3 | `ABVFP/0c12618c85-float_req_bl_0682a_true-unreach-call.c_13.md`, `ALIA/4c97df26e7-piVC_bd0142.md`, `ALIA/bdd5eb546d-piVC_a04477.md` |
| 9 | 2 | `ABVFP/ea7e47b81e-float_req_bl_0620b_true-unreach-call.c_6.md`, `NIA/520443d627-183.md` |
| 8 | 5 | `ABVFP/189893bdbb-float_req_bl_0530b_true-unreach-call.c_2.md`, `ALIA/499ffa55ba-piVC_2186b5.md`, `LIA/ee94632839-138.md`, `QF_AUFLIA/a6831a3fb1-pp-TakenBranch-s2e.md`, `QF_S/1ac968b76c-benchmark_0286.md` |
| 7 | 2 | `ALIA/f6285a256e-piVC_849b63.md`, `QF_ALIA/76fabb1637-stack-invalid-6.md` |
| 6 | 1 | `LIA/07d23f440c-076.md` |
| 5 | 1 | `NIA/d2baf9a6e3-184.md` |
| 4 | 1 | `QF_ALIA/60d1a1277d-qlock.induction.25.md` |
| 3 | 4 | `QF_ALIA/28114b6375-qlock-bug2-10.md`, `QF_ALIA/96eb0f0ccb-qlock.base.20.md`, `QF_ALIA/b1092fb93e-qlock.base.30.md`, `QF_ALIA/d6617f16d8-qlock.induction.16.md` |
| 0 | 8 | `LIA/01b211cc37-fcp_167_173_179.md`, `LIA/4935b59fa2-137.md`, `LIA/a60b6e08c6-fcp_197_199.md`, `NRA/722eaea277-strassen-hard.md`, `QF_AUFLIA/088a334a0f-storecomm_invalid_t3_pp_sf_ai_00060_004.cvc.md`, `QF_AUFLIA/3d0fe3ca5c-swap_invalid_t3_pp_sf_ai_00006_004.cvc.md`, `QF_AUFLIA/41d269aaaa-storecomm_invalid_t3_pp_sf_ni_00010_008.cvc.md`, `QF_AUFLIA/e387ddf96f-storecomm_invalid_t1_pp_sf_ai_00020_001.cvc.md` |

## 4. 复杂度与结构因素分析

这里的 clause 数是 CNF-Bench 文件的非空行数；literal 数按每行析取项估算。它们衡量表示规模，但不能完整代表理论推理难度。下表按三模型合计成功次数分组。

| 跨模型成功组 | 题数 | clauses 中位数 | literals 中位数 | CNF字符中位数 | SMT2字节中位数 | 量词出现中位数 |
|---|---:|---:|---:|---:|---:|---:|
| 稳定（15/15） | 36 | 2 | 2 | 884 | 2110 | 1 |
| 较强（10–14/15） | 33 | 13 | 26 | 2832 | 3100 | 2 |
| 边界（5–9/15） | 11 | 36 | 90 | 15505 | 6921 | 2 |
| 困难（0–4/15） | 13 | 234 | 234 | 37992 | 17040 | 0 |

### Golden status 与理论类型

| 维度 | 用例数 | 最终成功次数 | 最大次数 | 成功率 |
|---|---:|---:|---:|---:|
| logic=ABVFP | 9 | 102 | 135 | 75.56% |
| logic=ALIA | 12 | 144 | 180 | 80.00% |
| logic=LIA | 12 | 116 | 180 | 64.44% |
| logic=NIA | 12 | 156 | 180 | 86.67% |
| logic=NRA | 12 | 162 | 180 | 90.00% |
| logic=QF_ALIA | 11 | 94 | 165 | 56.97% |
| logic=QF_AUFLIA | 12 | 103 | 180 | 57.22% |
| logic=QF_NIRA | 1 | 15 | 15 | 100.00% |
| logic=QF_S | 12 | 165 | 180 | 91.67% |
| status=sat | 45 | 417 | 675 | 61.78% |
| status=unsat | 48 | 640 | 720 | 88.89% |

### 结论与原因解释

1. **Codex 在分类和证书两个阶段都最稳定。** 它的 Accuracy 为 96.56%，SAT witness rate 为 80.84%；Flash 分别为 86.67% 与 73.54%，Pro 为 76.56% 与 63.64%。因此模型间差距不只是 SAT/UNSAT 判断，也来自把 SAT 推理落实为可执行赋值的能力。
2. **UNSAT 与 SAT 的评分非对称。** UNSAT 命中 golden answer 即成功，而 SAT 还必须产生完整、语法正确且满足全部约束的 witness。因此 SAT 题的最终成功率天然同时受分类、模型构造、类型编码和 cvc5 校验影响；不能把 SAT 失败全部解释成逻辑判断失败。
3. **理论结构比单纯 clause 数更关键。** QF_AUFLIA 同时涉及数组、整数线性算术以及 store/select 一致性，多个模型即使判断 SAT 正确，也容易遗漏数组默认值或索引关系；LIA 中带量词或需要构造大量整数关系的题也会降低 witness 成功率。相反，部分 clause 很多但局部约束规律重复的题仍可能稳定成功。
4. **QF_ALIA 是主要分类弱点之一。** 三模型该逻辑 Accuracy 明显分化，说明数组与线性整数算术组合不仅影响 witness，也影响 verdict。ALIA 中的量词进一步增加全称条件与有限 witness 之间的推理负担。
5. **NRA/NIA 的表现说明‘非线性’不必然等于失败。** 本样本中的 NRA 分类非常稳定，NIA 也相对较好；这更可能反映所抽取实例具有可识别结构或容易构造的解，而不是模型已普遍掌握任意非线性算术。结论不能外推到整个 SMT-LIB 分布。
6. **浮点/位向量的主要风险在精确编码。** ABVFP 中分类通常较准，但 DeepSeek 尤其 Pro 的 witness rate 较低，常见瓶颈是浮点特殊值、舍入模式、位宽与精确常量格式，而不是只看公式长度。
7. **重复运行波动是重要信号。** 3/5、2/5 一类题表示模型已有部分能力但推理链或输出格式不稳定；0/5 且三模型共同失败的题才更像当前提示与输出协议下的系统性能力缺口。

## 5. 最终判断

在当前 93 题样本上，模型最可靠的是结构规律明显、赋值规模有限、证书容易完整表达的 CNF(T)；最不可靠的是数组与整数算术组合、带量词的全局约束，以及需要精确浮点/大规模数组 witness 的 SAT 题。Codex 5.6 Sol 的能力边界最宽，DeepSeek V4 Flash 次之，V4 Pro 在本批配置下最弱。复杂度不能仅用 clause 数排序：理论组合、量词、需要赋值的符号数量、精确数值编码和重复结构，都会显著改变难度。

报告中的相关性是对本批 93 题的描述性分析，不构成因果证明。后续批次应在每种 logic 内按 clause、符号数、量词深度与 witness 大小分层采样，才能更严格地估计大模型可处理的复杂度阈值。
