"""验证评判引擎的正确性"""
import json
import os
import subprocess
import sys
import tempfile

JUDGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands", "judge", "judge.py")
PROBLEMS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")

def run_judge(problem_dir, code, timeout=5):
    """运行评判引擎并返回结果"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(code)
        code_path = f.name
    try:
        result = subprocess.run(
            [sys.executable, JUDGE, "--problem", problem_dir, "--code", code_path, "--timeout", str(timeout)],
            capture_output=True, text=True, encoding='utf-8'
        )
        return json.loads(result.stdout)
    finally:
        os.unlink(code_path)

def print_result(name, result):
    """打印评判结果"""
    passed = result["passed"]
    total = result["total"]
    score = result["total_score"]
    verdicts = [f'{r["verdict"]}({r["case"]})' for r in result["results"]]
    status = "PASS" if passed == total else "EXPECTED" if score < 100 else "FAIL"
    print(f"  {'  '}{name}: {score}/100  {passed}/{total}  [{', '.join(verdicts)}]")

def verify():
    print("=" * 60)
    print("验证评判引擎 (judge.py)")
    print("=" * 60)

    all_passed = True

    # ---- Test 1: 070-爬楼梯 正确代码 ----
    print("\n[Test 1] 070-爬楼梯 - 正确代码 (应全 AC)")
    correct_climbing = """
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
    result = run_judge(os.path.join(PROBLEMS, "070-climbing-stairs"), correct_climbing)
    print_result("爬楼梯-正确", result)
    if result["total_score"] != 100:
        print("  FAIL: expected 100/100")
        all_passed = False

    # ---- Test 2: 070-爬楼梯 错误代码 ----
    print("\n[Test 2] 070-爬楼梯 - 错误代码 (应 WA)")
    wrong_climbing = """
import sys
input = lambda: sys.stdin.readline()
n = int(input())
print(n)  # 错误：直接输出 n 而非斐波那契
"""
    result = run_judge(os.path.join(PROBLEMS, "070-climbing-stairs"), wrong_climbing)
    print_result("爬楼梯-错误", result)
    if result["total_score"] == 100:
        print("  FAIL: should not be 100/100")
        all_passed = False

    # ---- Test 3: 053-最大子数组和 正确代码 ----
    print("\n[Test 3] 053-最大子数组和 - 正确代码 (应全 AC)")
    correct_maxsub = """
import sys
input = lambda: sys.stdin.readline()
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print(max(dp))
"""
    result = run_judge(os.path.join(PROBLEMS, "053-maximum-subarray"), correct_maxsub)
    print_result("最大子数组-正确", result)
    if result["total_score"] != 100:
        print("  FAIL: expected 100/100")
        all_passed = False

    # ---- Test 4: 空代码 (应 CE) ----
    print("\n[Test 4] 070-爬楼梯 - 空代码 (应 CE)")
    empty_code = "\n# empty\n"
    result = run_judge(os.path.join(PROBLEMS, "070-climbing-stairs"), empty_code)
    print_result("爬楼梯-空代码", result)
    if result["total_score"] != 0:
        print("  FAIL: expected 0/100 for empty code")
        all_passed = False
    if result["results"][0]["verdict"] != "CE":
        print("  FAIL: expected CE for empty code")
        all_passed = False

    # ---- Test 5: class Solution 遗留 (应警告但仍运行) ----
    print("\n[Test 5] 070-爬楼梯 - class Solution 遗留 (应警告)")
    leetcode_style = """
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# 这是 LeetCode 格式，不会正确运行
import sys
input = lambda: sys.stdin.readline()
n = int(input())
print(Solution().climbStairs(n))
"""
    result = run_judge(os.path.join(PROBLEMS, "070-climbing-stairs"), leetcode_style)
    print_result("爬楼梯-LeetCode格式", result)
    has_warning = any("class Solution" in w for w in result["precheck"]["warnings"])
    if not has_warning:
        print("  FAIL: expected warning about class Solution")
        all_passed = False

    # ---- Test 6: 121-买卖股票 正确代码 ----
    print("\n[Test 6] 121-买卖股票 - 正确代码 (应全 AC)")
    correct_stock = """
import sys
input = lambda: sys.stdin.readline()
n = int(input())
prices = list(map(int, input().split()))
min_price = prices[0]
max_profit = 0
for p in prices[1:]:
    max_profit = max(max_profit, p - min_price)
    min_price = min(min_price, p)
print(max_profit)
"""
    result = run_judge(os.path.join(PROBLEMS, "121-best-time-to-buy-sell-stock"), correct_stock)
    print_result("买卖股票-正确", result)
    if result["total_score"] != 100:
        print("  FAIL: expected 100/100")
        all_passed = False

    # ---- Test 7: 200-岛屿数量 正确代码 ----
    print("\n[Test 7] 200-岛屿数量 - 正确代码 (应全 AC)")
    correct_islands = """
import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        row = input().split()
        grid.append(row)

    visited = [[False]*n for _ in range(m)]
    count = 0
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    print(count)

solve()
"""
    result = run_judge(os.path.join(PROBLEMS, "200-number-of-islands"), correct_islands)
    print_result("岛屿数量-正确", result)
    if result["total_score"] != 100:
        print("  FAIL: expected 100/100")
        all_passed = False

    # ---- Test 8: 206-反转链表 正确代码 ----
    print("\n[Test 8] 206-反转链表 - 正确代码 (应全 AC)")
    correct_reverse = """
import sys
input = lambda: sys.stdin.readline()
n = int(input())
if n == 0:
    pass
else:
    nums = list(map(int, input().split()))
    nums.reverse()
    print(*nums)
"""
    result = run_judge(os.path.join(PROBLEMS, "206-reverse-linked-list"), correct_reverse)
    print_result("反转链表-正确", result)
    if result["total_score"] != 100:
        print("  FAIL: expected 100/100")
        all_passed = False

    # ---- Test 9: 预检 - 无 input() ----
    print("\n[Test 9] 预检 - 无 input() 读入 (应警告)")
    no_input = """
n = 5
print(n)
"""
    result = run_judge(os.path.join(PROBLEMS, "070-climbing-stairs"), no_input)
    has_warning = any("input()" in w for w in result["precheck"]["warnings"])
    print(f"  Warnings: {result['precheck']['warnings']}")
    if not has_warning:
        print("  FAIL: expected warning about missing input()")
        all_passed = False

    # ---- Test 10: 207-课程表 正确代码 ----
    print("\n[Test 10] 207-课程表 - 正确代码 (应全 AC)")
    correct_course = """
import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        adj[b].append(a)
        indeg[a] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    print("Yes" if cnt == n else "No")

solve()
"""
    result = run_judge(os.path.join(PROBLEMS, "207-course-schedule"), correct_course)
    print_result("课程表-正确", result)
    if result["total_score"] != 100:
        print("  FAIL: expected 100/100")
        all_passed = False

    # ---- Summary ----
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    verify()
