import sys
input = sys.stdin.readline
m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
target = int(input())
# 从右上角出发: 当前数大往左, 小往下
i, j = 0, n - 1
found = False
while i < m and j >= 0:
    if g[i][j] == target:
        found = True; break
    elif g[i][j] > target:
        j -= 1
    else:
        i += 1
print('true' if found else 'false')
