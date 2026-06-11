import sys
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

    result = []
    def inorder(u):
        if u == 0:
            return
        inorder(left[u])
        result.append(str(u))
        inorder(right[u])

    inorder(1)
    print(' '.join(result))

solve()
