import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
l, r = 0, n - 1
while l < r:
    mid = (l + r) // 2
    if nums[mid] > nums[r]:
        l = mid + 1
    else:
        r = mid
print(nums[l])
