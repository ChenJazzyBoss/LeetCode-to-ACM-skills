import sys
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()
    n = len(s)
    ans = 0
    for center in range(2 * n - 1):
        l = center // 2
        r = l + (center % 2)
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    print(ans)

solve()
