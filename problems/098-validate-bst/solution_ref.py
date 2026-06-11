import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    if n == 0:
        print("true")
        return
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if left[u] == 0:
            left[u] = v
        else:
            right[u] = v

    # 节点 i 的值就是 i，检查 BST 性质
    def validate(u, lo, hi):
        if u == 0:
            return True
        if u <= lo or u >= hi:
            return False
        return validate(left[u], lo, u) and validate(right[u], u, hi)

    print("true" if validate(1, -1, n + 1) else "false")

solve()
