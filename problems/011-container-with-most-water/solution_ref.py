import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    height = list(map(int, input().split()))
    left, right = 0, n - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    print(max_area)

solve()
