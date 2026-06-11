"""验证 Task 4-6: Skill 层基础设施完整性检查

Skill 本身是 AI 驱动的，无法用脚本自动化测试。
但可以验证 Skill 依赖的所有基础设施是否就绪：
  1. index.json 可读、标签可筛选、有目录存在的题目可枚举
  2. judge.py 可正常调用并返回有效 JSON
  3. problem.md 格式正确、可被 AI 解析
  4. 知识点匹配逻辑（模糊匹配）的基础数据正确
  5. 模板文件存在且语法正确
"""
import json
import os
import subprocess
import sys
import random
import tempfile

BASE = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = os.path.join(BASE, "problems")
JUDGE = os.path.join(BASE, "commands", "judge", "judge.py")
FETCH = os.path.join(BASE, "commands", "fetch", "fetch_helper.py")
TEMPLATES = os.path.join(BASE, "templates")
SKILL = os.path.join(BASE, ".claude", "skills", "acm.md")

def load_index():
    with open(os.path.join(PROBLEMS, "index.json"), encoding="utf-8") as f:
        return json.load(f)

def available_problems(index):
    """返回有本地目录的题目（Skill 抽题池）"""
    avail = []
    for p in index:
        if os.path.isdir(os.path.join(PROBLEMS, p["dir"])):
            avail.append(p)
    return avail

def verify():
    print("=" * 60)
    print("验证 Task 4-6: Skill 层基础设施")
    print("=" * 60)

    all_passed = True

    # ---- Test 1: Skill 文件存在且结构完整 ----
    print("\n[Test 1] Skill 文件 (acm.md)")
    assert os.path.isfile(SKILL), "acm.md not found"
    with open(SKILL, encoding="utf-8") as f:
        skill = f.read()
    required_sections = [
        "出题官", "裁判", "教练",
        "/acm quiz", "/acm practice", "/acm fetch",
        "/acm judge", "/acm hint", "/acm review",
        "渐进提示", "薄弱知识点", "测验汇总报告",
        "ACM 格式转换", "测试用例生成规则",
    ]
    for section in required_sections:
        assert section in skill, f"acm.md missing section: {section}"
    print(f"  PASS: acm.md exists ({len(skill.splitlines())} lines), all sections present")

    # ---- Test 2: 抽题池 ----
    print("\n[Test 2] 抽题池（有本地目录的题目）")
    index = load_index()
    avail = available_problems(index)
    assert len(avail) >= 10, f"Expected >= 10 available problems, got {len(avail)}"
    print(f"  PASS: {len(avail)}/{len(index)} problems have local directories")

    # ---- Test 3: 随机抽题（模拟 Skill 抽题逻辑）----
    print("\n[Test 3] 随机抽题逻辑")
    # 3a: 无筛选随机抽 3 题
    sampled = random.sample(avail, 3)
    ids = [p["id"] for p in sampled]
    assert len(set(ids)) == 3, "Duplicate IDs in sample"
    print(f"  PASS: random 3/10 (IDs: {ids})")

    # 3b: 按标签筛选
    dp_problems = [p for p in avail if "动态规划" in p["tags"]]
    assert len(dp_problems) >= 1, "No 动态规划 problems available"
    print(f"  PASS: 动态规划 filter → {len(dp_problems)} problems: {[p['title'] for p in dp_problems]}")

    # 3c: 边界 - 请求超过可用数
    if len(dp_problems) < len(avail):
        try_count = len(avail) + 5
        sampled_all = random.sample(avail, min(try_count, len(avail)))
        assert len(sampled_all) == len(avail), "Should sample all available"
        print(f"  PASS: over-request capped to {len(avail)} available problems")

    # ---- Test 4: 知识点标签完整性 ----
    print("\n[Test 4] 知识点标签")
    all_tags = set()
    for p in index:
        all_tags.update(p["tags"])
    expected_tags = [
        "BFS", "DFS", "动态规划", "双指针", "二叉树", "链表",
        "哈希表", "数组", "回溯算法", "贪心算法",
    ]
    for tag in expected_tags:
        assert tag in all_tags, f"Missing expected tag: {tag}"
    print(f"  PASS: {len(all_tags)} unique tags, all expected tags present")

    # ---- Test 5: problem.md 格式验证 ----
    print("\n[Test 5] problem.md 格式（所有可用题目）")
    required_fields = ["输入格式", "输出格式", "样例"]
    for p in avail:
        md_path = os.path.join(PROBLEMS, p["dir"], "problem.md")
        with open(md_path, encoding="utf-8") as f:
            content = f.read()
        for field in required_fields:
            assert field in content, f"{p['dir']}: missing '{field}'"
    print(f"  PASS: all {len(avail)} problem.md files have required fields")

    # ---- Test 6: judge.py 评判端到端 ----
    print("\n[Test 6] judge.py 端到端（Skill 调用路径）")
    # 模拟 Skill 保存用户代码并调用 judge
    test_code = """
import sys
input = lambda: sys.stdin.readline()
n = int(input())
if n <= 2:
    print(n)
else:
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)
"""
    problem_dir = os.path.join(PROBLEMS, "070-climbing-stairs")
    sub_path = os.path.join(problem_dir, "submission.py")
    with open(sub_path, "w", encoding="utf-8") as f:
        f.write(test_code)

    result = subprocess.run(
        [sys.executable, JUDGE, "--problem", problem_dir, "--code", sub_path],
        capture_output=True, text=True, encoding="utf-8"
    )
    judge_output = json.loads(result.stdout)

    assert judge_output["total_score"] == 100, f"Expected 100, got {judge_output['total_score']}"
    assert judge_output["passed"] == judge_output["total"], "Not all cases passed"
    assert "precheck" in judge_output, "Missing precheck in output"
    assert "results" in judge_output, "Missing results in output"

    # 清理
    os.unlink(sub_path)
    print(f"  PASS: judge → 100/100, {judge_output['passed']}/{judge_output['total']} AC")

    # ---- Test 7: 参考解全部可用 ----
    print("\n[Test 7] 所有参考解可评判")
    for p in avail:
        ref = os.path.join(PROBLEMS, p["dir"], "solution_ref.py")
        assert os.path.isfile(ref), f"{p['dir']}: missing solution_ref.py"
        result = subprocess.run(
            [sys.executable, JUDGE, "--problem", os.path.join(PROBLEMS, p["dir"]), "--code", ref],
            capture_output=True, text=True, encoding="utf-8"
        )
        judge_out = json.loads(result.stdout)
        assert judge_out["total_score"] == 100, \
            f"{p['dir']}: ref solution scored {judge_out['total_score']}/100"
    print(f"  PASS: all {len(avail)} reference solutions score 100/100")

    # ---- Test 8: 模板文件 ----
    print("\n[Test 8] 模板文件")
    expected_templates = ["basic.py", "multi_case.py", "matrix.py", "graph.py", "tree.py", "fast_io.py"]
    for t in expected_templates:
        tpath = os.path.join(TEMPLATES, t)
        assert os.path.isfile(tpath), f"Missing template: {t}"
        # 验证语法
        result = subprocess.run(
            [sys.executable, "-c", f"import py_compile; py_compile.compile(r'{tpath}', doraise=True)"],
            capture_output=True, text=True
        )
        assert result.returncode == 0, f"Template {t} has syntax error: {result.stderr}"
    print(f"  PASS: {len(expected_templates)} templates exist and compile")

    # ---- Test 9: fetch_helper 可调用 ----
    print("\n[Test 9] fetch_helper.py 可调用")
    result = subprocess.run(
        [sys.executable, FETCH, "--check", "1"],
        capture_output=True, text=True, encoding="utf-8"
    )
    out = json.loads(result.stdout)
    assert out["found"] == True and out["source"] == "builtin"
    result2 = subprocess.run(
        [sys.executable, FETCH, "--check", "9999"],
        capture_output=True, text=True, encoding="utf-8"
    )
    out2 = json.loads(result2.stdout)
    assert out2["found"] == False
    print("  PASS: fetch_helper --check works (1=found, 9999=not found)")

    # ---- Test 10: 测验报告数据可生成 ----
    print("\n[Test 10] 模拟测验报告数据")
    # 模拟 Skill 维护的训练记录
    training_log = [
        {"id": 70, "title": "爬楼梯", "tags": ["动态规划"], "score": 100, "verdict": "AC"},
        {"id": 200, "title": "岛屿数量", "tags": ["BFS", "DFS"], "score": 67, "verdict": "WA"},
        {"id": 206, "title": "反转链表", "tags": ["链表"], "score": 0, "verdict": "SKIPPED"},
    ]

    # 统计知识点通过率
    tag_stats = {}
    for log in training_log:
        for tag in log["tags"]:
            if tag not in tag_stats:
                tag_stats[tag] = {"total": 0, "ac": 0}
            tag_stats[tag]["total"] += 1
            if log["verdict"] == "AC":
                tag_stats[tag]["ac"] += 1

    # 验证统计逻辑
    assert tag_stats["动态规划"] == {"total": 1, "ac": 1}
    assert tag_stats["BFS"] == {"total": 1, "ac": 0}
    assert tag_stats["链表"] == {"total": 1, "ac": 0}

    # 识别薄弱点
    weak = [tag for tag, s in tag_stats.items() if s["total"] > 0 and s["ac"] / s["total"] < 0.5]
    assert "BFS" in weak
    assert "动态规划" not in weak

    total_questions = len(training_log)
    ac_count = sum(1 for l in training_log if l["verdict"] == "AC")
    wa_count = sum(1 for l in training_log if l["verdict"] == "WA")
    skip_count = sum(1 for l in training_log if l["verdict"] == "SKIPPED")

    print(f"  PASS: 模拟 3 题测验 → AC:{ac_count} WA:{wa_count} Skip:{skip_count}")
    print(f"  PASS: 薄弱知识点: {weak}")
    print(f"  PASS: 知识点统计: {tag_stats}")

    # ---- Summary ----
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL TESTS PASSED!")
        print("\n✅ Skill 基础设施验证完成:")
        print(f"   - acm.md: 完整 ({len(skill.splitlines())} 行)")
        print(f"   - 抽题池: {len(avail)} 道题可用")
        print(f"   - 标签体系: {len(all_tags)} 个知识点")
        print(f"   - 评判引擎: 正常")
        print(f"   - 模板: {len(expected_templates)} 个")
        print(f"   - 报告逻辑: 验证通过")
    else:
        print("SOME TESTS FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    verify()
