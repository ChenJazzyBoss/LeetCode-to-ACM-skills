import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
q = deque()
fresh = 0
for i in range(m):
    for j in range(n):
        if g[i][j] == 2: q.append((i,j))
        elif g[i][j] == 1: fresh += 1
minutes = 0
while q and fresh:
    minutes += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and g[nx][ny]==1:
                g[nx][ny] = 2
                fresh -= 1
                q.append((nx,ny))
print(minutes if fresh==0 else -1)
