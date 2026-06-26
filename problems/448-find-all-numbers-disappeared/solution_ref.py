import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    seen = [False] * (n + 1)
    for x in nums:
        if 1 <= x <= n:
            seen[x] = True
    res = [i for i in range(1, n + 1) if not seen[i]]
    print(*res) if res else print()

solve()
