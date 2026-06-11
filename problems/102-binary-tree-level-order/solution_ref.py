import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    if n == 0:
        print()
        return
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if left[u] == 0:
            left[u] = v
        else:
            right[u] = v

    q = deque([1])
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            u = q.popleft()
            level.append(str(u))
            if left[u]:
                q.append(left[u])
            if right[u]:
                q.append(right[u])
        print(' '.join(level))

solve()
