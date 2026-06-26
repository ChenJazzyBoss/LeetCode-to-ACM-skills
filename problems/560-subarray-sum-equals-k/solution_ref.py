import sys
from collections import defaultdict
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    prefix = defaultdict(int)
    prefix[0] = 1
    cur = 0
    ans = 0
    for x in nums:
        cur += x
        ans += prefix[cur - k]
        prefix[cur] += 1
    print(ans)

solve()
