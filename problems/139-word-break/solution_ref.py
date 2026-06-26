import sys
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()
    m = int(input())
    words = [input().strip() for _ in range(m)]
    wordset = set(words)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordset:
                dp[i] = True
                break
    print("True" if dp[n] else "False")

solve()
