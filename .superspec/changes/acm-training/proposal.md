# acm-training

## Why

构建完整的 ACM 训练 Skill：帮助用户从 LeetCode 格式过渡到 ACM 竞赛格式。大模型扮演出题官、裁判、教练三种角色，提供沉浸式的 ACM 训练体验。

## What Changes

- 新增 `acm.md` Skill 主文件（出题官 + 教练角色）
- 新增评判引擎脚本（裁判角色，确定性执行）
- 新增内置 Hot 100 题库数据
- 新增随机测验功能
- 整合已有 `templates/` 模板

## Capabilities

1. **built-in-problem-bank** — 内置 Hot 100 题库，离线可用
2. **quiz-system** — 随机测验系统（1/3/5 题），聊天式交互
3. **judge-engine** — 代码评判引擎（AC/WA/RE/TLE/CE + 打分）
4. **coach-feedback** — 教练反馈（错误分析 + 修复建议 + 薄弱点）
5. **online-fetch** — 在线抓取非内置题目（用户按需触发）

## Impact

- 新建文件：`acm.md`、`commands/judge/`、`problems/`
- 修改文件：`README.md`（更新使用说明）
- 依赖已有：`templates/` 目录
