#!/usr/bin/env python3
"""
在线抓取辅助工具

提供以下功能：
1. 检查题号是否在本地（内置 + 缓存）
2. 验证参考解是否正确（用示例输入运行并对比输出）
3. 用参考解批量生成 .out 文件
4. 缓存题目数据到 problems/ 目录

用法:
  python fetch_helper.py --check <题号>              # 检查题号是否存在本地
  python fetch_helper.py --verify-ref <题目目录>       # 验证参考解
  python fetch_helper.py --gen-outs <题目目录>         # 用参考解生成 .out
  python fetch_helper.py --cache <题号> <slug> <题目目录>  # 缓存到 problems/
"""

import argparse
import json
import os
import subprocess
import sys

PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "problems")


def check_local(problem_id: int) -> dict:
    """
    检查题号是否在本地（内置 + 在线缓存）。
    返回 {"found": bool, "source": str, "dir": str}
    """
    index_path = os.path.join(PROBLEMS_DIR, "index.json")
    if os.path.isfile(index_path):
        with open(index_path, encoding="utf-8") as f:
            index = json.load(f)
        for item in index:
            if item["id"] == problem_id:
                problem_dir = os.path.join(PROBLEMS_DIR, item["dir"])
                if os.path.isdir(problem_dir):
                    return {"found": True, "source": "builtin", "dir": item["dir"]}
                # 在索引中但目录不存在（未填充数据）
                return {"found": False, "source": "builtin-index-only", "dir": item["dir"]}

    # 检查在线缓存（不在 index.json 中但目录存在）
    padded = str(problem_id).zfill(3)
    for entry in os.listdir(PROBLEMS_DIR):
        entry_path = os.path.join(PROBLEMS_DIR, entry)
        if os.path.isdir(entry_path) and entry.startswith(padded + "-"):
            return {"found": True, "source": "online-cache", "dir": entry}

    return {"found": False, "source": None, "dir": None}


def verify_reference_solution(problem_dir: str, sample_input: str, sample_output: str) -> dict:
    """
    验证参考解是否正确。
    返回 {"valid": bool, "actual_output": str, "error": str}
    """
    ref_path = os.path.join(problem_dir, "solution_ref.py")
    if not os.path.isfile(ref_path):
        return {"valid": False, "actual_output": "", "error": "solution_ref.py not found"}

    try:
        proc = subprocess.run(
            [sys.executable, ref_path],
            input=sample_input,
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8',
        )
        if proc.returncode != 0:
            return {"valid": False, "actual_output": proc.stdout,
                    "error": f"Runtime error: {proc.stderr[:500]}"}

        # 对比输出（trim 模式）
        actual_lines = [line.strip() for line in proc.stdout.split('\n')
                        if line.strip()]
        expected_lines = [line.strip() for line in sample_output.split('\n')
                          if line.strip()]

        if actual_lines == expected_lines:
            return {"valid": True, "actual_output": proc.stdout, "error": ""}
        else:
            diff = []
            for i, (a, e) in enumerate(zip(actual_lines, expected_lines)):
                if a != e:
                    diff.append(f"Line {i+1}: expected '{e}', got '{a}'")
            if len(actual_lines) != len(expected_lines):
                diff.append(f"Line count: expected {len(expected_lines)}, got {len(actual_lines)}")
            return {"valid": False, "actual_output": proc.stdout,
                    "error": "Output mismatch: " + "; ".join(diff)}

    except subprocess.TimeoutExpired:
        return {"valid": False, "actual_output": "", "error": "Timeout (10s)"}
    except Exception as e:
        return {"valid": False, "actual_output": "", "error": str(e)}


def generate_outputs(problem_dir: str) -> dict:
    """
    用参考解为 tests/ 下所有 .in 文件生成对应的 .out 文件。
    跳过已有 .out 的文件（除非 --force）。
    返回 {"generated": int, "skipped": int, "errors": [...]}
    """
    ref_path = os.path.join(problem_dir, "solution_ref.py")
    tests_dir = os.path.join(problem_dir, "tests")

    if not os.path.isfile(ref_path):
        return {"generated": 0, "skipped": 0, "errors": ["solution_ref.py not found"]}
    if not os.path.isdir(tests_dir):
        return {"generated": 0, "skipped": 0, "errors": ["tests/ directory not found"]}

    generated = 0
    skipped = 0
    errors = []

    in_files = sorted([f for f in os.listdir(tests_dir) if f.endswith('.in')])

    for in_file in in_files:
        out_file = in_file.replace('.in', '.out')
        out_path = os.path.join(tests_dir, out_file)
        in_path = os.path.join(tests_dir, in_file)

        with open(in_path, encoding='utf-8') as f:
            input_data = f.read()

        try:
            proc = subprocess.run(
                [sys.executable, ref_path],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8',
            )
            if proc.returncode != 0:
                errors.append(f"{in_file}: runtime error - {proc.stderr[:200]}")
                skipped += 1
                continue

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(proc.stdout)
            generated += 1

        except subprocess.TimeoutExpired:
            errors.append(f"{in_file}: timeout")
            skipped += 1
        except Exception as e:
            errors.append(f"{in_file}: {e}")
            skipped += 1

    return {"generated": generated, "skipped": skipped, "errors": errors}


def cache_problem(problem_id: int, slug: str, source_dir: str) -> dict:
    """
    将题目数据缓存到 problems/ 目录。
    同时在 index.json 中添加在线缓存标记（source: online-fetch）。
    """
    padded = str(problem_id).zfill(3)
    dir_name = f"{padded}-{slug}"
    target_dir = os.path.join(PROBLEMS_DIR, dir_name)

    if os.path.isdir(target_dir):
        return {"cached": False, "error": f"Directory already exists: {dir_name}"}

    # 复制源目录到 problems/
    import shutil
    shutil.copytree(source_dir, target_dir)

    # 在 index.json 中添加条目（如果不存在）
    index_path = os.path.join(PROBLEMS_DIR, "index.json")
    index = []
    if os.path.isfile(index_path):
        with open(index_path, encoding='utf-8') as f:
            index = json.load(f)

    # 检查是否已存在
    if any(item["id"] == problem_id for item in index):
        return {"cached": True, "dir": dir_name, "note": "Already in index"}

    # 添加新条目
    new_entry = {
        "id": problem_id,
        "title": slug.replace("-", " ").title(),
        "slug": slug,
        "difficulty": "unknown",
        "tags": [],
        "inputMode": "basic",
        "dir": dir_name,
        "source": "online-fetch"
    }
    index.append(new_entry)
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    return {"cached": True, "dir": dir_name}


def main():
    parser = argparse.ArgumentParser(description="在线抓取辅助工具")
    parser.add_argument("--check", type=int, help="检查题号是否在本地")
    parser.add_argument("--verify-ref", help="验证参考解（传入题目目录）")
    parser.add_argument("--sample-in", help="示例输入（配合 --verify-ref）")
    parser.add_argument("--sample-out", help="示例输出（配合 --verify-ref）")
    parser.add_argument("--gen-outs", help="用参考解生成 .out（传入题目目录）")
    parser.add_argument("--cache", nargs=3, metavar=("ID", "SLUG", "DIR"),
                        help="缓存题目到 problems/")
    args = parser.parse_args()

    if args.check:
        result = check_local(args.check)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif args.verify_ref:
        if not args.sample_in or not args.sample_out:
            print("Error: --sample-in and --sample-out required with --verify-ref",
                  file=sys.stderr)
            sys.exit(1)
        result = verify_reference_solution(args.verify_ref, args.sample_in, args.sample_out)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif args.gen_outs:
        result = generate_outputs(args.gen_outs)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif args.cache:
        pid, slug, src_dir = args.cache
        result = cache_problem(int(pid), slug, src_dir)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
