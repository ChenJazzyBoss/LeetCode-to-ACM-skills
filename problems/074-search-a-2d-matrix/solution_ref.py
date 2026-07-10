import sys
input = sys.stdin.readline
m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
target = int(input())
nums = [x for row in g for x in row]
l, r = 0, len(nums) - 1
found = False
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        found = True; break
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
print('true' if found else 'false')
