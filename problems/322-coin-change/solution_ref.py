import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
    print(dp[amount] if dp[amount] != float('inf') else -1)

solve()
