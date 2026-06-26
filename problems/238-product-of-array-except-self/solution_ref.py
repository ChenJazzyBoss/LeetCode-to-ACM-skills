import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    res = [1]*n
    pre = 1
    for i in range(n):
        res[i] = pre
        pre *= nums[i]
    suf = 1
    for i in range(n-1,-1,-1):
        res[i] *= suf
        suf *= nums[i]
    print(*res)

solve()
