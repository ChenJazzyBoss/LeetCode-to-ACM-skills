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
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) == n:
        print(*order)
    else:
        print()

solve()
