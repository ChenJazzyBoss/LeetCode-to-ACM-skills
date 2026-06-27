# LeetCode-to-ACM Skills 🎯

> 一个 Claude Code Skill — 扮演 ACM 竞赛的**裁判 + 教练 + 出题官**，帮你从 LeetCode 函数式刷题过渡到 ACM 输入输出格式。

## 项目定位

```
你（选手）                    Skill（裁判 + 教练 + 出题官）
   │                                │
   │  ── 出题 / 抓题 ────────────→  │ 随机出题 或 在线抓取力扣原题，转成 ACM 格式
   │                                │
   │  ←── 题面 + 文件位置 ────────  │ 在 workspace/<日期>/ 建好练手文件
   │                                │
   │  ── 写好代码，"提交" ────────→  │ 逐用例运行，对比输出，判定 AC/WA/RE
   │                                │
   │  ←── 判题报告 + 修复建议 ────  │ 错误定位 + 教练反馈 + 追加训练日志
```

## 核心功能

| 命令 | 角色 | 说明 |
|------|------|------|
| `/acm teach` | 教练 | 讲解 ACM 输入输出范式（input/print/map/split）与模板用法 |
| `/acm practice <题号>` | 出题官 | 指定题号开始练习 |
| `/acm quiz` | 出题官 | 随机测验（1/3/5 题 + 知识点筛选），逐题作答 |
| `/acm fetch <题号>` | 出题官 | 在线抓取非内置题，转 ACM 格式并缓存 |
| `/acm judge` | 裁判 | 评判用户提交的代码（AC/WA/RE/TLE/CE） |
| `/acm hint` | 教练 | 渐进式提示（方向 → 方法 → 细节，三层） |
| `/acm review` | 教练 | 生成训练总结 + 薄弱知识点报告 |

## 与 LeetCode 的区别

| | LeetCode | ACM |
|---|----------|-----|
| 输入 | 函数参数 `def twoSum(nums, target)` | `input()` 从 stdin 读 |
| 输出 | `return` 返回值 | `print()` 到 stdout |
| 代码结构 | `class Solution:` | 直接写顶层代码 |
| 多组测试 | 不用管 | 可能要循环处理 |
| 评判方式 | 平台自动跑 | 管道输入 + 输出对比 |

## 评判机制

**判定类型**

| 判定 | 含义 | 触发条件 |
|------|------|----------|
| 🟢 AC | 正确 | 输出逐行 trim 后完全匹配 |
| 🟡 WA | 答案错误 | 输出不匹配（含行数不一致） |
| 🔴 RE | 运行错误 | 抛出异常 |
| 🟠 TLE | 超时 | 超过时限（默认 5 秒） |
| ⚪ CE | 编译错误 | 语法错误 |

**打分**：等权计分，每通过一个用例得 `100 / 用例数` 分。

**评判方式**（管道输入 → 捕获输出 → 与预期对比 → 逐用例打分）：
```bash
echo "5
1 2 3 4 5" | python solution.py
```

## 内置题库

`problems/` 下内置 **100 道**力扣经典题，每题包含：
- `problem.md` — ACM 格式题面（输入格式 / 输出格式 / 样例 / 数据范围）
- `solution_ref.py` — 参考解（均经评判引擎验证 100/100）
- `tests/` — 3 组测试用例（`01-basic` 样例 / `02-edge` 边界 / `03-random` 随机）

**难度分布**：Easy 21 / Medium 64 / Hard 15
**知识点覆盖**：30 个标签（动态规划、二叉树、链表、双指针、BFS/DFS、栈、堆、滑动窗口、前缀和、字典树、拓扑排序、单调栈、贪心……）

## 训练工作区

用户的练手代码与训练记录放在 `workspace/`（已 gitignore，私人草稿本，不进公开仓库）：

```
workspace/
└── 2026-06-27/                      ← 按日期组织
    ├── 070-climbing-stairs.py       ← 用户代码（Skill 自动建好，含题面+模板）
    ├── log.md                       ← 追加型日志：每次评判的时分+判定+解析+问答
    └── overview.md                  ← 当日总览（说"生成总览"时由 Skill 读 log 生成）
```

## 目录结构

```
LeetCode-to-ACM-skills/
├── acm.md                        # Skill 主文件（裁判+教练+出题官，权威源）
├── .claude/skills/acm.md         # Skill 加载副本（本地用，gitignore）
├── README.md                     # 本文件
├── .gitignore
├── commands/
│   ├── judge/judge.py            # 评判引擎（确定性，独立可执行）
│   └── fetch/fetch_helper.py     # 在线抓取辅助工具（检查/缓存/生成用例）
├── problems/
│   ├── index.json                # 100 题索引（题号/难度/标签/输入模式）
│   └── 001-two-sum/ ...          # 每题一个目录
├── templates/                    # ACM 输入输出模板（6 种）
│   ├── basic.py                  #   单组数据
│   ├── multi_case.py             #   多组测试
│   ├── matrix.py                 #   矩阵
│   ├── graph.py                  #   图
│   ├── tree.py                   #   树
│   └── fast_io.py                #   快速读入
├── verify_*.py                   # 4 个验证脚本（题库/评判/抓取/Skill 基础设施）
└── workspace/                    # 训练工作区（gitignore）
```

## 验证

四个验证脚本，全部通过：

```bash
python verify_problems.py    # 题库结构与用例答案
python verify_judge.py       # 评判引擎端到端
python verify_fetch.py       # 抓取辅助工具
python verify_skill.py       # Skill 基础设施（acm.md + 100 题参考解全 AC）
```

> ⚠️ Windows 下需设置 UTF-8 环境：`set PYTHONUTF8=1`（GBK 终端打印 emoji 会报错）。

## 开发流程

本项目使用 [superSpec](https://github.com/ChenJazzyBoss/superSpec) 驱动开发，规范文件见 `.superspec/`。

## License

MIT
