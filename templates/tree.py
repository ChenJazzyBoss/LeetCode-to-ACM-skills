# ============ ACM Python 树输入模板 ============
# 适用：n 个节点的树，输入 n-1 条边
#
# 输入格式：
#   n
#   u1 v1
#   u2 v2
#   ...
#   u(n-1) v(n-1)
#
# 示例输入（5 节点）：
#   5
#   1 2
#   1 3
#   2 4
#   2 5
#
# 注：ACM 中树没有 TreeNode 结构体，用邻接表 + DFS 遍历

import sys
input = lambda: sys.stdin.readline()
sys.setrecursionlimit(10 ** 6)

def solve():
    n = int(input())
    g = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # ----- DFS 遍历 -----
    def dfs(u, fa):
        depth = 1
        for v in g[u]:
            if v != fa:
                depth = max(depth, dfs(v, u) + 1)
        return depth

    ans = dfs(1, 0)  # 根节点为 1
    print(ans)

solve()
