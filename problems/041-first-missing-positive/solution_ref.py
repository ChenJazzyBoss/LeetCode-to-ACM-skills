import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
# 原地哈希: 把 nums[i] 放到 nums[i]-1 位置
for i in range(n):
    while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
for i in range(n):
    if nums[i] != i + 1:
        print(i + 1); break
else:
    print(n + 1)
