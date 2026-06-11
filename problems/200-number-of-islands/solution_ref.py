import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        row = input().split()
        grid.append(row)

    visited = [[False] * n for _ in range(m)]
    count = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    print(count)

solve()
