"""验证内置题库数据的正确性"""
import json
import os
import sys

PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")

def verify_index():
    """验证 index.json 格式和完整性"""
    with open(os.path.join(PROBLEMS_DIR, "index.json"), encoding="utf-8") as f:
        index = json.load(f)

    assert isinstance(index, list), "index.json should be a list"
    assert len(index) == 100, f"Expected 100 problems, got {len(index)}"

    ids = set()
    for item in index:
        assert "id" in item, f"Missing id: {item}"
        assert "title" in item, f"Missing title: {item}"
        assert "slug" in item, f"Missing slug: {item}"
        assert "difficulty" in item, f"Missing difficulty: {item}"
        assert "tags" in item, f"Missing tags: {item}"
        assert "inputMode" in item, f"Missing inputMode: {item}"
        assert "dir" in item, f"Missing dir: {item}"
        assert item["difficulty"] in ("easy", "medium", "hard"), f"Invalid difficulty: {item['difficulty']}"
        assert item["inputMode"] in ("basic", "multi_case", "matrix", "graph", "tree", "fast_io"), f"Invalid inputMode: {item['inputMode']}"
        assert item["id"] not in ids, f"Duplicate id: {item['id']}"
        ids.add(item["id"])

    print(f"✅ index.json: {len(index)} problems, all fields valid, no duplicate ids")
    return index

def verify_problem_dir(index):
    """验证每个有目录的题目"""
    for item in index:
        problem_dir = os.path.join(PROBLEMS_DIR, item["dir"])
        if not os.path.isdir(problem_dir):
            continue  # 只验证已创建目录的题目

        # 检查 problem.md
        problem_md = os.path.join(problem_dir, "problem.md")
        assert os.path.isfile(problem_md), f"{item['dir']}: missing problem.md"

        with open(problem_md, encoding="utf-8") as f:
            content = f.read()
        assert "输入格式" in content, f"{item['dir']}: problem.md missing 输入格式"
        assert "输出格式" in content, f"{item['dir']}: problem.md missing 输出格式"
        assert "样例" in content, f"{item['dir']}: problem.md missing 样例"

        # 检查 tests/ 目录
        tests_dir = os.path.join(problem_dir, "tests")
        assert os.path.isdir(tests_dir), f"{item['dir']}: missing tests/ directory"

        in_files = [f for f in os.listdir(tests_dir) if f.endswith(".in")]
        out_files = [f for f in os.listdir(tests_dir) if f.endswith(".out")]

        assert len(in_files) >= 3, f"{item['dir']}: expected >= 3 test cases, got {len(in_files)}"
        assert len(in_files) == len(out_files), f"{item['dir']}: .in count ({len(in_files)}) != .out count ({len(out_files)})"

        # 检查每个 .in 有对应的 .out
        for in_file in in_files:
            out_file = in_file.replace(".in", ".out")
            assert out_file in out_files, f"{item['dir']}: {in_file} has no matching .out file"

        print(f"  ✅ {item['dir']}: problem.md + {len(in_files)} test cases")

def verify_test_cases():
    """验证测试用例内容的正确性 - 用已知正确答案校验"""
    results = []

    # 070-爬楼梯: f(n) = fib(n+1)
    test_cases = {
        "070-climbing-stairs": [
            ("01-basic", "3"),    # n=3 -> 3
            ("02-edge", "1"),     # n=1 -> 1
            ("03-random", "89"),  # n=10 -> 89
        ],
        "053-maximum-subarray": [
            ("01-basic", "6"),    # [-2,1,-3,4,-1,2,1,-5,4] -> 6
            ("02-edge", "-1"),    # [-1] -> -1
            ("03-special", "23"), # [5,4,-1,7,8] -> 23
        ],
        "121-best-time-to-buy-sell-stock": [
            ("01-basic", "5"),    # [7,1,5,3,6,4] -> 5
            ("02-edge", "0"),     # [7,6,4,3,1] -> 0
            ("03-random", "7"),   # [2,4,1,5,3,6,4,8] -> 7
        ],
        "200-number-of-islands": [
            ("01-basic", "3"),
            ("02-edge", "1"),
            ("03-special", "0"),
        ],
        "207-course-schedule": [
            ("01-basic", "Yes"),
            ("02-edge", "No"),
            ("03-special", "Yes"),
        ],
    }

    for problem_dir, cases in test_cases.items():
        for case_name, expected in cases:
            out_path = os.path.join(PROBLEMS_DIR, problem_dir, "tests", f"{case_name}.out")
            with open(out_path, encoding="utf-8") as f:
                actual = f.read().strip()

            status = "✅" if actual == expected else "❌"
            results.append((problem_dir, case_name, expected, actual, status))
            print(f"  {status} {problem_dir}/{case_name}: expected={expected}, actual={actual}")

    failed = [r for r in results if r[4] == "❌"]
    return failed

if __name__ == "__main__":
    print("=" * 50)
    print("🔍 验证内置题库数据")
    print("=" * 50)

    print("\n📋 Step 1: 验证 index.json")
    index = verify_index()

    print("\n📋 Step 2: 验证题目目录结构")
    verify_problem_dir(index)

    print("\n📋 Step 3: 验证测试用例答案")
    failed = verify_test_cases()

    print("\n" + "=" * 50)
    if failed:
        print(f"❌ 验证失败: {len(failed)} 个测试用例答案不正确")
        for r in failed:
            print(f"  {r[0]}/{r[1]}: expected={r[2]}, actual={r[3]}")
        sys.exit(1)
    else:
        print("✅ 全部验证通过!")
