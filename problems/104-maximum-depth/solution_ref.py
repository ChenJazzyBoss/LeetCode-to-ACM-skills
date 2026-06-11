import sys
input = lambda: sys.stdin.readline()
sys.setrecursionlimit(10 ** 6)

def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    def dfs(u, fa):
        depth = 1
        for v in g[u]:
            if v != fa:
                depth = max(depth, dfs(v, u) + 1)
        return depth

    print(dfs(1, 0))

solve()
