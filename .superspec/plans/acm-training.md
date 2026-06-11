# ACM Training — 实现计划

## 依赖关系

```
built-in-problem-bank ──→ judge-engine ──→ quiz-system
                      ──→ online-fetch ──→ quiz-system
                                              ──→ coach-feedback
```

## 任务列表

### Task 1: 题目数据结构和索引 (built-in-problem-bank)
- [ ] 1.1 创建 `problems/` 目录结构
- [ ] 1.2 创建 `problems/index.json` 索引文件（100 题）
- [ ] 1.3 创建第一批内置题目（10 道代表性题目，覆盖各输入模式）
- [ ] 1.4 定义 `problem.md` 统一格式规范
- [ ] 1.5 定义测试用例 `.in`/`.out` 文件格式
- 验收：index.json 可被正确解析，题目可通过题号和知识点检索

### Task 2: 评判引擎 (judge-engine)
- [ ] 2.1 创建 `commands/judge/judge.py` 主评判脚本
- [ ] 2.2 实现代码结构预检（检测 class Solution / input / print）
- [ ] 2.3 实现管道执行（stdin 输入 + stdout 捕获 + 超时控制）
- [ ] 2.4 实现输出对比（trim 逐行对比 + 差异报告）
- [ ] 2.5 实现判定与打分（AC/WA/RE/TLE/CE + 等权计分）
- [ ] 2.6 实现结构化 JSON 结果输出
- 验收：用内置题目的测试用例 + 已知正确/错误代码实际运行评判

### Task 3: 在线抓取与格式转换 (online-fetch)
- [ ] 3.1 在 Skill 中实现在线抓取逻辑（使用 web 工具读取力扣页面）
- [ ] 3.2 实现 LeetCode → ACM 格式转换（AI 驱动）
- [ ] 3.3 实现自动测试用例生成（AI 驱动 + 已知算法验证）
- [ ] 3.4 实现本地缓存（保存到 problems/ 目录）
- 验收：抓取一道非内置题目，转换为 ACM 格式，生成测试用例并缓存

### Task 4: 随机测验系统 (quiz-system)
- [ ] 4.1 在 Skill 中实现 `/acm quiz` 交互流程
- [ ] 4.2 实现模式选择（1/3/5 题 + 知识点筛选）
- [ ] 4.3 实现逐题作答流程（展示题面 → 等待提交 → 调用评判 → 下一题）
- [ ] 4.4 实现测验总结报告生成
- [ ] 4.5 实现随机抽取策略（无重复 + 优先未做题）
- 验收：完整跑通一轮 3 题小测验

### Task 5: 教练反馈 (coach-feedback)
- [ ] 5.1 在 Skill 中实现 WA/RE 错误分析（行级定位 + 原因推断）
- [ ] 5.2 实现修复建议（最小改动优先 + 渐进引导）
- [ ] 5.3 实现渐进式提示系统（方向 → 方法 → 细节，三层）
- [ ] 5.4 实现薄弱知识点追踪（记录评判历史 + 生成报告）
- 验收：提交一个有 bug 的代码，教练能给出有意义的分析和修复建议

### Task 6: Skill 主文件整合 (acm.md)
- [ ] 6.1 重写 `acm.md` Skill 主文件，整合所有模块
- [ ] 6.2 实现命令路由（/acm teach / fetch / quiz / practice / judge / hint / review）
- [ ] 6.3 更新 README.md 使用说明
- 验收：所有命令均可正常触发对应功能

## 执行顺序

```
Task 1 ──→ Task 2 ──→ Task 4 ──→ Task 5
         ──→ Task 3 ──↗             ──→ Task 6
```

- Task 1（题库）是基础，Task 2（评判）依赖 Task 1 的测试用例
- Task 3（在线抓取）可并行，不依赖 Task 2
- Task 4（测验）依赖 Task 1 + Task 2
- Task 5（教练反馈）依赖 Task 2 的评判结果
- Task 6（整合）最后做

## 里程碑

| 里程碑 | 完成条件 | 预计任务 |
|--------|----------|----------|
| M1: 核心可用 | 能出题 + 能评判 | Task 1 + Task 2 |
| M2: 在线扩展 | 能抓取非内置题 | + Task 3 |
| M3: 测验体验 | 能随机测验 | + Task 4 |
| M4: 完整体验 | 教练反馈 + Skill 整合 | + Task 5 + Task 6 |
