import sys
from collections import defaultdict
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    dp = defaultdict(int)
    dp[0] = 1
    for x in nums:
        ndp = defaultdict(int)
        for s, c in dp.items():
            ndp[s + x] += c
            ndp[s - x] += c
        dp = ndp
    print(dp[target])

solve()
