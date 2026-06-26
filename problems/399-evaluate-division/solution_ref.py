import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline()

def solve():
    m = int(input())
    graph = defaultdict(dict)
    for _ in range(m):
        a, b, v = input().split()
        v = float(v)
        graph[a][b] = v
        graph[b][a] = 1.0 / v
    q = int(input())
    queries = []
    for _ in range(q):
        a, b = input().split()
        queries.append((a, b))

    def query(a, b):
        if a not in graph or b not in graph:
            return -1.0
        if a == b:
            return 1.0
        visited = {a}
        dq = deque([(a, 1.0)])
        while dq:
            node, val = dq.popleft()
            for nxt, w in graph[node].items():
                if nxt == b:
                    return val * w
                if nxt not in visited:
                    visited.add(nxt)
                    dq.append((nxt, val * w))
        return -1.0

    for a, b in queries:
        r = query(a, b)
        print(f"{r:.2f}")

solve()
