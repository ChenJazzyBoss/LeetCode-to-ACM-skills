import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    print(*res)

solve()
