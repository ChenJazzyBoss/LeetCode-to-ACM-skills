# ============ ACM Python 矩阵输入模板 ============
# 适用：二维数组 / 网格
#
# 输入格式：
#   m n
#   a11 a12 ... a1n
#   a21 a22 ... a2n
#   ...
#   am1 am2 ... amn
#
# 示例输入：
#   3 4
#   1 1 0 0
#   0 1 1 0
#   0 0 1 0
#
# 示例输出：
#   3

import sys
input = lambda: sys.stdin.readline()

def solve():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)

    # ----- TODO: 你的逻辑 -----

    ans = 0
    print(ans)

solve()
