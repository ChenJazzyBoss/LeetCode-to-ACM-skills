#!/usr/bin/env python3
"""
ACM 代码评判引擎

用法:
  python judge.py --problem <题目目录> --code <代码文件> [--timeout 5]

输出 JSON 格式的评判报告:
{
  "precheck": {"warnings": [...], "errors": [...]},
  "results": [
    {"case": "01-basic", "type": "basic", "verdict": "AC", "score": 20, ...},
    ...
  ],
  "total_score": 80,
  "max_score": 100,
  "passed": 4,
  "total": 5
}
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time


# ============ 常量 ============

VERDICT_AC = "AC"
VERDICT_WA = "WA"
VERDICT_RE = "RE"
VERDICT_TLE = "TLE"
VERDICT_CE = "CE"

DEFAULT_TIMEOUT = 5  # 秒


# ============ 代码结构预检 ============

def precheck_code(code: str) -> dict:
    """
    检查代码结构是否符合 ACM 格式。
    返回 {"warnings": [...], "errors": [...]}
    """
    warnings = []
    errors = []

    # 空代码检查
    stripped_lines = [line.strip() for line in code.split('\n')
                      if line.strip() and not line.strip().startswith('#')]
    if not stripped_lines:
        errors.append("代码为空或仅包含注释")
        return {"warnings": warnings, "errors": errors}

    # 检查 class Solution 遗留
    if re.search(r'class\s+Solution\s*:', code):
        warnings.append("LeetCode 格式残留: 包含 class Solution，建议改为顶层代码")

    # 检查是否有 input 读入
    has_input = bool(re.search(r'input\s*\(|sys\.stdin', code))
    if not has_input:
        warnings.append("未检测到 input() 或 sys.stdin 读入，ACM 格式需要从 stdin 读取输入")

    # 检查是否有 print 输出
    has_output = bool(re.search(r'print\s*\(|sys\.stdout', code))
    if not has_output:
        warnings.append("未检测到 print() 或 sys.stdout 输出，ACM 格式需要输出到 stdout")

    # 检查主流程中是否有 return（非函数内部的 return）
    lines = code.split('\n')
    in_function = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('def '):
            in_function = True
        elif stripped and not stripped[0].isspace() and not stripped.startswith('#'):
            in_function = False
        if not in_function and re.match(r'return\s', stripped):
            warnings.append("主流程中使用了 return，ACM 格式应使用 print() 输出")

    return {"warnings": warnings, "errors": errors}


# ============ 测试用例加载 ============

def load_test_cases(problem_dir: str) -> list:
    """
    从题目目录加载测试用例。
    返回 [{"name": "01-basic", "type": "basic", "input": "...", "expected": "..."}]
    """
    tests_dir = os.path.join(problem_dir, "tests")
    if not os.path.isdir(tests_dir):
        return []

    in_files = sorted([f for f in os.listdir(tests_dir) if f.endswith('.in')])
    cases = []

    for in_file in in_files:
        out_file = in_file.replace('.in', '.out')
        out_path = os.path.join(tests_dir, out_file)

        if not os.path.isfile(out_path):
            continue  # 跳过不完整的用例对

        name = in_file.replace('.in', '')
        # 从文件名提取类型（如 01-basic -> basic）
        parts = name.split('-', 1)
        case_type = parts[1] if len(parts) > 1 else "unknown"

        with open(os.path.join(tests_dir, in_file), encoding='utf-8') as f:
            input_data = f.read()

        with open(out_path, encoding='utf-8') as f:
            expected = f.read()

        cases.append({
            "name": name,
            "type": case_type,
            "input": input_data,
            "expected": expected,
        })

    return cases


# ============ 代码执行 ============

def run_single_case(code: str, input_data: str, timeout: int) -> dict:
    """
    执行单个测试用例。
    返回 {"output": str, "stderr": str, "exit_code": int, "time_ms": int, "verdict": str}
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False,
                                      encoding='utf-8') as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        start = time.time()
        proc = subprocess.run(
            [sys.executable, tmp_path],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        elapsed_ms = int((time.time() - start) * 1000)

        if proc.returncode != 0:
            return {
                "output": proc.stdout,
                "stderr": proc.stderr,
                "exit_code": proc.returncode,
                "time_ms": elapsed_ms,
                "verdict": VERDICT_RE,
            }

        return {
            "output": proc.stdout,
            "stderr": proc.stderr,
            "exit_code": 0,
            "time_ms": elapsed_ms,
            "verdict": None,  # 待对比后确定
        }

    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "stderr": "Time Limit Exceeded",
            "exit_code": -1,
            "time_ms": timeout * 1000,
            "verdict": VERDICT_TLE,
        }
    except SyntaxError as e:
        return {
            "output": "",
            "stderr": str(e),
            "exit_code": -1,
            "time_ms": 0,
            "verdict": VERDICT_CE,
        }
    finally:
        os.unlink(tmp_path)


# ============ 输出对比 ============

def compare_output(actual: str, expected: str) -> dict:
    """
    对比实际输出和预期输出。
    先按行 split，逐行 trim 后对比。
    返回 {"match": bool, "diff": str}
    """
    actual_lines = actual.split('\n')
    expected_lines = expected.split('\n')

    # 去除尾部空行
    while actual_lines and actual_lines[-1].strip() == '':
        actual_lines.pop()
    while expected_lines and expected_lines[-1].strip() == '':
        expected_lines.pop()

    # 逐行 trim 对比
    max_len = max(len(actual_lines), len(expected_lines))
    diff_parts = []

    for i in range(max_len):
        act = actual_lines[i].strip() if i < len(actual_lines) else '<missing>'
        exp = expected_lines[i].strip() if i < len(expected_lines) else '<missing>'

        if act != exp:
            diff_parts.append(f"Line {i + 1}: expected '{exp}', got '{act}'")

    if not diff_parts:
        return {"match": True, "diff": ""}
    else:
        return {"match": False, "diff": '\n'.join(diff_parts)}


# ============ 主评判流程 ============

def judge(problem_dir: str, code_path: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """主评判函数"""

    # 1. 读取代码
    with open(code_path, encoding='utf-8') as f:
        code = f.read()

    # 2. 代码结构预检
    precheck = precheck_code(code)

    # 如果代码为空，直接返回 CE
    if precheck["errors"]:
        cases = load_test_cases(problem_dir)
        results = []
        for case in cases:
            results.append({
                "case": case["name"],
                "type": case["type"],
                "verdict": VERDICT_CE,
                "score": 0,
                "time_ms": 0,
                "detail": precheck["errors"][0],
            })
        return {
            "precheck": precheck,
            "results": results,
            "total_score": 0,
            "max_score": 100,
            "passed": 0,
            "total": len(cases),
        }

    # 3. 加载测试用例
    cases = load_test_cases(problem_dir)
    if not cases:
        return {
            "precheck": precheck,
            "results": [],
            "total_score": 0,
            "max_score": 0,
            "passed": 0,
            "total": 0,
            "error": "No test cases found",
        }

    # 4. 逐用例运行
    # 等权计分：100 分 / 用例数，余数分给前几个用例
    base_score = 100 // len(cases)
    remainder = 100 % len(cases)
    results = []

    for idx, case in enumerate(cases):
        run_result = run_single_case(code, case["input"], timeout)

        if run_result["verdict"]:
            # 已经判定（RE/TLE/CE）
            verdict = run_result["verdict"]
            detail = run_result["stderr"][:500] if run_result["stderr"] else ""
        else:
            # 需要对比输出
            cmp = compare_output(run_result["output"], case["expected"])
            if cmp["match"]:
                verdict = VERDICT_AC
                detail = ""
            else:
                verdict = VERDICT_WA
                detail = cmp["diff"]

        case_score = base_score + (1 if idx < remainder else 0)
        results.append({
            "case": case["name"],
            "type": case["type"],
            "verdict": verdict,
            "score": case_score if verdict == VERDICT_AC else 0,
            "time_ms": run_result["time_ms"],
            "detail": detail,
        })

    # 5. 汇总
    total_score = sum(r["score"] for r in results)
    passed = sum(1 for r in results if r["verdict"] == VERDICT_AC)

    return {
        "precheck": precheck,
        "results": results,
        "total_score": total_score,
        "max_score": 100,
        "passed": passed,
        "total": len(results),
    }


# ============ CLI 入口 ============

def main():
    parser = argparse.ArgumentParser(description="ACM 代码评判引擎")
    parser.add_argument("--problem", required=True, help="题目目录路径")
    parser.add_argument("--code", required=True, help="用户代码文件路径")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                        help="超时时间（秒），默认 5")
    args = parser.parse_args()

    result = judge(args.problem, args.code, args.timeout)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
