import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    if n <= 1:
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

    def is_mirror(a, b):
        if a == 0 and b == 0:
            return True
        if a == 0 or b == 0:
            return False
        return is_mirror(left[a], right[b]) and is_mirror(right[a], left[b])

    print("true" if is_mirror(left[1], right[1]) else "false")

solve()
