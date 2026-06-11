"""验证参考解和辅助工具的正确性"""
import json
import os
import subprocess
import sys

PROBLEMS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")
JUDGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands", "judge", "judge.py")
FETCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands", "fetch", "fetch_helper.py")

def run_cmd(args):
    result = subprocess.run(
        [sys.executable] + args,
        capture_output=True, text=True, encoding='utf-8'
    )
    return json.loads(result.stdout)

def verify():
    print("=" * 60)
    print("验证 Task 3: 在线抓取辅助工具 + 参考解")
    print("=" * 60)

    all_passed = True

    # ---- Test 1: check 本地题号 ----
    print("\n[Test 1] --check 本地题号")
    r = run_cmd([FETCH, "--check", "1"])
    assert r["found"] == True and r["source"] == "builtin"
    r = run_cmd([FETCH, "--check", "9999"])
    assert r["found"] == False
    r = run_cmd([FETCH, "--check", "70"])
    assert r["found"] == True
    print("  PASS: check 1(builtin), 70(builtin), 9999(not found)")

    # ---- Test 2: 参考解通过评判引擎 ----
    print("\n[Test 2] 参考解全部通过评判 (10道题)")
    problems = [
        "001-two-sum", "015-3sum", "070-climbing-stairs",
        "053-maximum-subarray", "121-best-time-to-buy-sell-stock",
        "200-number-of-islands", "056-merge-intervals",
        "207-course-schedule", "104-maximum-depth",
        "206-reverse-linked-list",
    ]
    for p in problems:
        ref = os.path.join(PROBLEMS, p, "solution_ref.py")
        assert os.path.isfile(ref), f"{p}: missing solution_ref.py"
        result = run_cmd([JUDGE, "--problem", os.path.join(PROBLEMS, p), "--code", ref])
        score = result["total_score"]
        passed = result["passed"]
        total = result["total"]
        status = "PASS" if score == 100 else "FAIL"
        print(f"  {status} {p}: {score}/100  {passed}/{total}")
        if score != 100:
            all_passed = False

    # ---- Test 3: verify-ref 验证参考解 ----
    print("\n[Test 3] --verify-ref 验证参考解")
    r = run_cmd([
        FETCH, "--verify-ref", os.path.join(PROBLEMS, "070-climbing-stairs"),
        "--sample-in", "3\n", "--sample-out", "3\n"
    ])
    assert r["valid"] == True, f"Expected valid=True, got {r}"
    print(f"  PASS: 070-climbing-stairs ref solution verified (input=3, expected=3)")

    # ---- Test 4: verify-ref 错误代码 ----
    print("\n[Test 4] --verify-ref 错误参考解")
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8', dir=os.path.join(PROBLEMS, "070-climbing-stairs")) as f:
        f.write("print(99999)\n")
        bad_ref = f.name
    # 临时替换
    real_ref = os.path.join(PROBLEMS, "070-climbing-stairs", "solution_ref.py")
    import shutil
    shutil.move(real_ref, real_ref + ".bak")
    shutil.move(bad_ref, real_ref)

    r = run_cmd([
        FETCH, "--verify-ref", os.path.join(PROBLEMS, "070-climbing-stairs"),
        "--sample-in", "3\n", "--sample-out", "3\n"
    ])
    shutil.move(real_ref, bad_ref)
    shutil.move(real_ref + ".bak", real_ref)
    os.unlink(bad_ref)

    assert r["valid"] == False, f"Expected valid=False, got {r}"
    print(f"  PASS: bad ref correctly rejected ({r['error'][:50]})")

    # ---- Test 5: gen-outs 生成 .out ----
    print("\n[Test 5] --gen-outs 用参考解生成 .out")
    # 用 001-two-sum 测试，先把 .out 移走再重新生成
    test_dir = os.path.join(PROBLEMS, "001-two-sum", "tests")
    out_files = [f for f in os.listdir(test_dir) if f.endswith('.out')]
    # 备份
    for f in out_files:
        shutil.move(os.path.join(test_dir, f), os.path.join(test_dir, f + ".bak"))

    r = run_cmd([FETCH, "--gen-outs", os.path.join(PROBLEMS, "001-two-sum")])
    assert r["generated"] == 3, f"Expected 3 generated, got {r}"

    # 对比生成的和备份的
    for f in out_files:
        gen_path = os.path.join(test_dir, f)
        bak_path = os.path.join(test_dir, f + ".bak")
        with open(gen_path, encoding='utf-8') as gf:
            gen_content = gf.read().strip()
        with open(bak_path, encoding='utf-8') as bf:
            bak_content = bf.read().strip()
        assert gen_content == bak_content, f"{f}: gen output differs from original"
        # 清理：恢复备份
        os.unlink(gen_path)
        shutil.move(bak_path, gen_path)

    print(f"  PASS: generated 3 .out files, all match originals")

    # ---- Summary ----
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    verify()
