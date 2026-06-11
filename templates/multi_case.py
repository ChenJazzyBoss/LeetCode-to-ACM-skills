# ============ ACM Python 多组测试模板 ============
# 适用：第一行 T 表示组数，接下来 T 组数据
#
# 输入格式：
#   T
#   n
#   a1 a2 ... an
#   n
#   a1 a2 ... an
#   ...（共 T 组）
#
# 示例输入：
#   2
#   5
#   1 2 3 4 5
#   3
#   10 20 30
#
# 示例输出：
#   15
#   60

import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    # ----- TODO: 你的逻辑 -----

    ans = sum(nums)
    print(ans)

T = int(input())
for _ in range(T):
    solve()
