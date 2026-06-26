import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    prev2 = prev1 = 0
    for x in nums:
        cur = max(prev1, prev2 + x)
        prev2 = prev1
        prev1 = cur
    print(prev1)

solve()
