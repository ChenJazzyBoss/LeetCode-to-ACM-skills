import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    dp = [0] + [float('inf')] * n
    i = 1
    while i * i <= n:
        sq = i * i
        for j in range(sq, n + 1):
            if dp[j - sq] + 1 < dp[j]:
                dp[j] = dp[j - sq] + 1
        i += 1
    print(dp[n])

solve()
