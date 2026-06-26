import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    arr = [1] + nums + [1]
    m = len(arr)
    dp = [[0]*m for _ in range(m)]
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], arr[i]*arr[k]*arr[j] + dp[i][k] + dp[k][j])
    print(dp[0][m-1])

solve()
