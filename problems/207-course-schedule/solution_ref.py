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
