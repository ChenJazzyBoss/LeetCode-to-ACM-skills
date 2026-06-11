import sys
input = lambda: sys.stdin.readline()

def solve():
    m, n = map(int, input().split())
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    print(dp[n - 1])

solve()
