import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline()

def solve():
    vals = list(map(int, input().split()))
    n = len(vals)
    val = [0] + vals  # 1-indexed
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    has_parent = [False] * (n + 1)
    for _ in range(n - 1):
        parts = input().split()
        p, c, side = int(parts[0]), int(parts[1]), parts[2]
        if side == 'L':
            left[p] = c
        else:
            right[p] = c
        has_parent[c] = True
    root = 1
    for i in range(1, n + 1):
        if not has_parent[i]:
            root = i
            break
    INF = float('-inf')
    ans = INF

    def gain(u):
        nonlocal ans
        if u == 0:
            return 0
        lg = max(gain(left[u]), 0)
        rg = max(gain(right[u]), 0)
        ans = max(ans, val[u] + lg + rg)
        return val[u] + max(lg, rg)

    gain(root)
    print(ans)

solve()
