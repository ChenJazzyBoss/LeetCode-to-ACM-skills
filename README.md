# LeetCode → ACM Skills 🎯

> 一个 [Claude Code](https://www.anthropic.com/claude-code) Skill —— 把 Claude 变成你的 **ACM 竞赛裁判 + 教练 + 出题官**，帮你从 LeetCode 函数式刷题无缝过渡到 ACM `stdin/stdout` 格式。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://docs.claude.com/en/docs/claude-code)
[![Problems](https://img.shields.io/badge/LeetCode%20Hot100-100%20%E9%A2%98-brightgreen)](problems/hot100-official.md)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)]()

---

## ✨ 为什么需要这个项目？

刷 LeetCode 和真正的 ACM/笔试/手撕代码场景之间，隔着一道**输入输出鸿沟**：

| | LeetCode | ACM / 笔试 / 手撕 |
|---|----------|-----|
| **输入** | 数据塞进函数参数 `def solve(nums, target)` | 自己用 `input()` 从 stdin 读 |
| **输出** | `return` 返回值 | `print()` 打到 stdout |
| **代码结构** | `class Solution:` | 直接写顶层代码 |
| **评判** | 平台自动跑 | 管道喂入数据 + 输出对比 |

很多算法功底扎实的人到了笔试/面试现场，**死在读输入、格式化输出、边界处理上**。这个 Skill 就是来补这一块的——你在 IDE 里写代码，Skill 出题、判题、记录、复盘，全流程闭环。

---

## 🎬 30 秒上手

```
你：抽道题
Skill：从 Hot100 中等题里随机抽 1 道，建好 workspace/<日期>/<题号>.py，
      给出文件的绝对路径 + ACM 题面（输入格式/输出格式/样例/数据范围）。
你：在 IDE 写完，说"提交"。
Skill：逐用例跑你的代码，对比输出，给出 AC/WA 报告 + 错误定位 + 修复建议，
      追加一条记录到 log.md。
```

**一句话：你只管写代码，其他的事 Skill 包了。**

---

## 🛠️ 核心命令

| 命令 | 角色 | 作用 |
|------|------|------|
| `/acm quiz` | 🎯 出题官 | 随机抽题（1/3/5 题，可选知识点筛选、可选复习模式） |
| `/acm practice <题号>` | 🎯 出题官 | 指定题号开始练习 |
| `/acm fetch <题号>` | 🎯 出题官 | 在线抓取非内置题，转 ACM 格式并缓存 |
| `/acm judge` | ⚖️ 裁判 | 评判用户刚提交的代码 |
| `/acm hint` | 👨‍🏫 教练 | 渐进式提示（方向 → 方法 → 细节，三层） |
| `/acm teach` | 👨‍🏫 教练 | 讲解 ACM 输入输出范式 + 模板用法 |
| `/acm review` | 👨‍🏫 教练 | 生成训练总结 + 薄弱知识点报告 |

---

## 📚 内置题库 — 官方 Hot100 全对齐

`problems/` 下内置 **LeetCode 官方最新版 Hot100 全部 100 题**（按 [studyplan/top-100-liked](https://leetcode.cn/studyplan/top-100-liked/) 对齐），每题包含：

- `problem.md` — ACM 格式题面（题目描述 / 输入格式 / 输出格式 / 样例 / 数据范围）
- `solution_ref.py` — 参考解（均经评判引擎验证 100/100）
- `tests/` — 3 组测试用例：`01-basic`（样例）/ `02-edge`（边界）/ `03-random`（随机）

**按官方分类组织**（完整列表见 [`problems/hot100-official.md`](problems/hot100-official.md)）：

```
哈希(3) · 双指针(4) · 滑动窗口(2) · 子串(3) · 普通数组(5) · 矩阵(4)
链表(14) · 二叉树(15) · 图论(4) · 回溯(8) · 二分查找(6) · 栈(5) · 堆(3)
贪心算法(4) · 动态规划(10) · 多维动态规划(5) · 技巧(5)
```

> 树/链表/设计类题目涉及自定义类（`TreeNode`/`ListNode`/`Trie` 等），已为它们预留目录与 ACM 协议模板，后续按需补全测试。

---

## ⚖️ 评判机制

### 判定类型

| 判定 | 含义 | 触发条件 |
|------|------|----------|
| 🟢 **AC** | 正确 | 输出逐行 trim 后完全匹配 |
| 🟡 **WA** | 答案错误 | 输出不匹配（含行数不一致） |
| 🔴 **RE** | 运行错误 | 抛出异常 |
| 🟠 **TLE** | 超时 | 超过时限（默认 5 秒） |
| ⚪ **CE** | 编译错误 | 语法错误 |

### 打分

等权计分，每通过一个用例得 `100 / 用例数` 分。评判输出 JSON：

```bash
python commands/judge/judge.py \
    --problem problems/001-two-sum \
    --code workspace/2026-07-09/001-two-sum.py
```

```json
{
  "results": [
    {"case": "01-basic", "verdict": "AC", "score": 34},
    {"case": "02-edge",  "verdict": "AC", "score": 33},
    {"case": "03-random","verdict": "AC", "score": 33}
  ],
  "total_score": 100, "passed": 3, "total": 3
}
```

评判引擎是**确定性、独立可执行**的——脱离 Claude 也能用，方便集成到 CI 或自己的刷题脚本。

---

## 🗂️ 训练工作区

用户的练手代码与训练记录放在 `workspace/`（已 gitignore，**私人草稿本不进仓库**）：

```
workspace/
└── 2026-07-09/                       ← 按日期组织
    ├── 042-trapping-rain-water.py    ← 用户代码（Skill 自动建好，含题面注释）
    ├── 200-number-of-islands-review.py  ← 复习题（带 -review 后缀）
    ├── log.md                        ← 追加型日志：每次评判的判定+解析+问答
    └── overview.md                   ← 当日总览（说"生成总览"时由 Skill 读 log 生成）
```

### 周期性复习机制

防止"做完就忘"。Skill 内置三种复习触发：

| 触发 | 规则 |
|------|------|
| **自动** | 每完成 5 道新题，下一题自动插 1 道复习题 |
| **每日首题** | 新一天开始时问一句"先复习一道热手？" |
| **主动** | 用户说"复习"/"来道复习题" 即触发 |

复习选题优先级：**曾经 WA 的题 > 距今 >3 天 > 随机**，同一题最多复习 2 次。

---

## 📁 项目结构

```
LeetCode-to-ACM-skills/
├── README.md                          # 本文件
├── LICENSE                            # MIT
├── .gitignore
├── .claude/skills/acm.md              # Skill 主文件（裁判+教练+出题官，权威源）
├── commands/
│   ├── judge/judge.py                 # 评判引擎（确定性，独立可执行）
│   └── fetch/fetch_helper.py          # 在线抓取辅助工具
├── problems/
│   ├── index.json                     # 100 题索引
│   ├── hot100-official.md             # 官方 Hot100 题单存档（按分类）
│   └── 001-two-sum/                   # 每题一个目录
│       ├── problem.md
│       ├── solution_ref.py
│       └── tests/{01-basic,02-edge,03-random}.{in,out}
├── templates/                         # ACM 输入输出模板（6 种）
│   ├── basic.py                       #   单组数据
│   ├── multi_case.py                  #   多组测试
│   ├── matrix.py                      #   矩阵
│   ├── graph.py                       #   图
│   ├── tree.py                        #   二叉树
│   └── fast_io.py                     #   快速读入
└── workspace/                         # 训练工作区（gitignore）
```

---

## 🚀 快速开始

### 1. 安装 [Claude Code](https://docs.claude.com/en/docs/claude-code)

### 2. 克隆本仓库

```bash
git clone https://github.com/ChenJazzyBoss/LeetCode-to-ACM-skills.git
cd LeetCode-to-ACM-skills
```

### 3. 把 `.claude/skills/acm.md` 放到你的 Claude Code 能识别的 skills 目录

（通常就在仓库内 `.claude/skills/`，Claude Code 打开本仓库即可加载。）

### 4. 在对话里直接说

```
抽道题                       → 随机出一道
复习                         → 来一道复习题
帮我讲讲 XXX 题              → 教练模式
```

或用斜杠命令 `/acm quiz`、`/acm practice <题号>`、`/acm judge`。

---

## 🔍 适合谁

- ✅ **LeetCode 刷了不少，但笔试/ACM 输入输出老是卡壳** 的人
- ✅ **算法思路有，但 Python 实现细节（边界/语法/格式）反复踩坑** 的人
- ✅ 想要**有教练复盘 + 周期复习** 的系统化刷题者
- ✅ 准备**国内大厂笔试 / 校招手撕代码** 的求职者

---

## ⚠️ 环境注意

- **Windows 编码**：终端默认 GBK，打印 emoji/读中文题面会 `UnicodeEncodeError`。涉及中文/emoji 的 Python 调用前设 `PYTHONUTF8=1`。
- **Python 版本**：3.9+（用了 `functools.cache` 装饰器）。

---

## 🧪 验证脚本

```bash
PYTHONUTF8=1 python verify_problems.py    # 题库结构与用例答案
PYTHONUTF8=1 python verify_judge.py       # 评判引擎端到端
PYTHONUTF8=1 python verify_fetch.py       # 抓取辅助工具
PYTHONUTF8=1 python verify_skill.py       # Skill 基础设施（100 题参考解全 AC）
```

---

## 🗺️ Roadmap

- [ ] 补全树/链表/设计类题目的 ACM 协议模板与测试用例
- [ ] 增加每周自动 overview（统计 AC 率 / 薄弱知识点趋势）
- [ ] 支持多语言评判（C++ / Java / Go）
- [ ] 在线抓取升级（自动识别题号 + 批量导入）

---

## 📜 License

[MIT](LICENSE)
