import sys
input = sys.stdin.readline
m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
rows = [any(g[i][j]==0 for j in range(n)) for i in range(m)]
cols = [any(g[i][j]==0 for i in range(m)) for j in range(n)]
for i in range(m):
    for j in range(n):
        if rows[i] or cols[j]:
            g[i][j] = 0
for row in g:
    print(*row)
