import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = sorted(nums)
    l, r = 0, n - 1
    while l <= r and nums[l] == sorted_nums[l]:
        l += 1
    while r >= l and nums[r] == sorted_nums[r]:
        r -= 1
    print(max(0, r - l + 1))

solve()
