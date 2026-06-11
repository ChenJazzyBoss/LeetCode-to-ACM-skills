import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    heights = list(map(int, input().split()))
    stack = []
    max_area = 0
    for i in range(n + 1):
        h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    print(max_area)

solve()
