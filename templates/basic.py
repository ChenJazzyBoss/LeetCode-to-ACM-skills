# ============ ACM Python 基础模板 ============
# 适用：单组数据输入
#
# 输入格式：
#   第一行：整数 n
#   第二行：n 个整数
#
# 示例输入：
#   5
#   1 2 3 4 5
#
# 示例输出：
#   15

import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    # ----- TODO: 你的逻辑 -----

    ans = 0
    print(ans)

solve()
