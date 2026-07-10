import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
target = int(input())
l, r = 0, n - 1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        print(mid); break
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
else:
    print(l)
