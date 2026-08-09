# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 项目概览

这是一个 **Codex Skill** 项目（不是独立应用）：核心交付物是根目录的 `acm.md` —— 一份让 Codex 扮演「ACM 竞赛裁判 + 教练 + 出题官」的指令文件，帮用户从 LeetCode 函数式刷题过渡到 ACM `stdin/stdout` 格式。

仓库语言为**简体中文**：README、`acm.md`、`problem.md`、注释、commit message 全为中文。新增内容请保持中文。仓库无 `package.json`、无构建系统，Python 侧零第三方依赖（纯标准库）。

## 常用命令

验证脚本（根目录，直接跑 Python，无测试框架）：

```bash
PYTHONUTF8=1 python verify_problems.py   # 题库结构与用例答案（⚠ 当前失败，见下）
PYTHONUTF8=1 python verify_judge.py      # 评判引擎端到端（✅ 通过）
PYTHONUTF8=1 python verify_fetch.py      # 抓取工具 + 参考解（✅ 通过）
PYTHONUTF8=1 python verify_skill.py      # Skill 基础设施（⚠ 当前失败，见下）
```

工具脚本：

```bash
# 评判用户代码（输出 JSON：precheck / results[] / total_score / passed / total）
python commands/judge/judge.py --problem problems/001-two-sum --code <用户代码.py> [--timeout 5]

# 在线抓取辅助：查本地 / 校验参考解 / 批量生成 .out / 缓存新题到 problems/
python commands/fetch/fetch_helper.py --check <题号>
python commands/fetch/fetch_helper.py --verify-ref <题目录> --sample-in <输入> --sample-out <期望>
python commands/fetch/fetch_helper.py --gen-outs <题目录>
python commands/fetch/fetch_helper.py --cache <题号> <slug> <源目录>

# 日期工具：北京时间(UTC+8)日期 / 当天 workspace 路径
python commands/date/date_helper.py [--workspace]
```

## 环境注意（Windows）

- 终端默认 GBK：打印 emoji / 读中文题面会 `UnicodeEncodeError`。**所有涉及中文/emoji 的 Python 调用前设 `PYTHONUTF8=1`**；读 JSON/中文文件一律显式 `encoding="utf-8"`。
- Python 3.9+（`acm.md` 提到 `functools.cache`）。

## 架构

### 核心交付物：`acm.md`（根目录，权威源）

Skill 主文件，定义三个角色（出题官 / 裁判 / 教练）、命令路由表（`/acm teach|practice|quiz|fetch|judge|hint|review`）与训练工作区机制。它通过相对路径定位工具与数据（`commands/`、`problems/`、`templates/` 与它同级）。

**⚠ 安装位置不一致**：README 项目结构图与 `verify_skill.py` 引用 `.Codex/skills/acm.md`，但该目录被 gitignore，仓库中不存在（本地仅有 gitignore 的 `settings.local.json`）。git 跟踪的 Skill 源文件是**根目录的 `acm.md`**。改 Skill 改根目录文件；如需让 Codex 在本仓库内加载该 Skill，须先复制/链接到 `.Codex/skills/acm.md`。

`acm.md` 中的关键行为约束（改动需保持一致，不要破坏）：
- **禁止作弊**：Skill 为用户生成的题面文件里绝不贴核心解法代码，只给题面 + 文字思路提示 + TODO；仅当用户明确说"给我答案"才在对话框给完整解法。
- **抽题策略**：以中等题为主（medium:easy:hard ≈ 7:2:1）；抽题池 = index.json 中目录真实存在的题；一轮内不重复。
- **训练记录**：`workspace/<日期>/log.md` 只追加不覆盖；`overview.md` 不自动生成，用户要求时才由 log 汇总。

### `commands/` — 确定性 Python 工具（被 acm.md 调用）

- `judge/judge.py` — 评判引擎。流程：结构预检（检测 `class Solution` 遗留 / 是否 `input()` / 是否 `print` / 顶层 `return`）→ 逐用例 stdin 管道执行 + 超时 → 输出逐行 trim 对比 → 等权计分（`100//用例数`，余数分给前几个用例）。判定 AC/WA/RE/TLE/CE。**独立、确定性、脱离 Codex 可执行**。
- `fetch/fetch_helper.py` — 本地题号查找、参考解校验、用参考解从 `.in` 生成 `.out`、把在线抓取的题缓存进 `problems/` 并在 index.json 追加条目。
- `date/date_helper.py` — 北京时间日期 + workspace 路径。

### `problems/` — 内置题库

- `index.json` — 102 条索引（最近一次提交从 100 扩到 102）。**⚠ 元数据与 problem.md 不同步**：`difficulty` 全为 `"medium"`、`tags` 空数组、`title` 空串，是占位值；每题真实元数据在各自 `problem.md` 头部（`**难度**` / `**知识点**` / `**输入模式**`）。
- `hot100-official.md` — 官方 Hot100 题单存档（按分类）。
- 每题一个目录 `NNN-slug/`，含：
  - `problem.md` — ACM 格式题面，必须含「输入格式 / 输出格式 / 样例」（另有「数据范围」）。
  - `solution_ref.py` — 参考解（须经评判引擎 100/100 验证）。
  - `tests/` — ≥3 组用例，每组 `NN-type.in` + `NN-type.out` 配对（`01-basic` 样例 / `02-edge` 边界 / `03-random` 随机）。

新增题的标准流程：写 `problem.md` + `solution_ref.py` → 手工造 `.in` → `fetch_helper.py --gen-outs` 用参考解生成 `.out` → `--verify-ref` 校验参考解。

### `templates/` — ACM 输入输出模板

6 个：`basic` / `multi_case` / `matrix` / `graph` / `tree` / `fast_io`，与题目 `inputMode` 对应，`/acm teach` 按需推荐。核心模式固定为 `import sys` + `input = lambda: sys.stdin.readline()`。

### `workspace/` — 训练工作区（gitignore）

按日期组织：`workspace/2026-07-09/{题号-slug.py, log.md, overview.md}`。用户私人草稿本，不进仓库。

### `.superspec/` — 规范驱动开发

含各功能 spec（题库 / 评判引擎 / 在线抓取 / 测验 / 教练反馈）与实现计划 `plans/acm-training.md`。`scripts/validate.js` 是 esbuild 打包产物（内含 zod），**不要直接编辑**。GitHub Actions `superspec-validate.yml` 校验 `.superspec/specs/**`，但它引用的 `npm ci` / `node bin/superspec.js` 在仓库内并不存在，CI 当前不可运行。

## 当前已知问题（动手前注意）

1. **`verify_problems.py` 失败**：断言 `len(index) == 100`，但 index.json 已扩到 102 条。改动题库时应同步更新该断言。
2. **`verify_skill.py` 失败**：断言 `.Codex/skills/acm.md` 存在，但它是 gitignore 的本地安装产物，干净 clone 上不存在。
3. **index.json 元数据是占位值**：与各 `problem.md` 头部的真实难度/知识点/输入模式不同步。若 Skill 的抽题/筛选逻辑依赖 `index.json` 的 `difficulty`/`tags`，当前实际拿到的都是占位数据。
