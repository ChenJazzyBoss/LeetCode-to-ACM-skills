# ============ ACM Python 图输入模板 ============
# 适用：n 个节点 m 条边的无向图
#
# 输入格式：
#   n m
#   u1 v1
#   u2 v2
#   ...
#   um vm
#
# 示例输入（5 节点 4 条边）：
#   5 4
#   1 2
#   1 3
#   2 4
#   3 5
#
# 节点编号从 1 开始

import sys
from collections import deque
input = lambda: sys.stdin.readline()
sys.setrecursionlimit(10 ** 6)

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]  # 邻接表，1-indexed

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)  # 无向图；有向图删掉这行

    # ----- TODO: BFS / DFS / 拓扑排序等 -----

    ans = 0
    print(ans)

solve()
