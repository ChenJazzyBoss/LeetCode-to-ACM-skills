import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    idx = {v: i for i, v in enumerate(inorder)}
    res = []
    pre_iter = iter(preorder)
    def build(lo, hi):
        if lo > hi:
            return
        val = next(pre_iter)
        mid = idx[val]
        build(lo, mid - 1)
        build(mid + 1, hi)
        res.append(val)
    build(0, n - 1)
    print(*res)

solve()
