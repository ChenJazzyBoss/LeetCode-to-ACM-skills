import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    lo = 0
    for i in range(n):
        if nums[i] != 0:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    print(*nums)

solve()
