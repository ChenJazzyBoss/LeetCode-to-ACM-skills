import sys
input = lambda: sys.stdin.readline()

def solve():
    first = input().split()
    rows, cols = map(int, first)
    grid = [input().strip() for _ in range(rows)]
    heights = [0] * cols
    best = 0
    for r in range(rows):
        for c in range(cols):
            heights[c] = heights[c] + 1 if grid[r][c] == '1' else 0
        # 单调栈求最大矩形（柱状图）
        stack = []
        h = heights + [0]
        for i, v in enumerate(h):
            while stack and h[stack[-1]] > v:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                best = max(best, h[top] * width)
            stack.append(i)
    print(best)

solve()
