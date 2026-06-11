import sys
input = lambda: sys.stdin.readline()

def solve():
    nums = list(map(int, input().split()))
    target = int(input())
    n = len(nums)
    if n == 0:
        print(-1, -1)
        return

    # 找左边界
    left, right = 0, n - 1
    first = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    first = left if left < n and nums[left] == target else -1

    if first == -1:
        print(-1, -1)
        return

    # 找右边界
    left, right = first, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    print(first, right)

solve()
