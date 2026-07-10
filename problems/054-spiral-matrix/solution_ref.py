import sys
input = sys.stdin.readline
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
ans = []
top, bot, lft, rgt = 0, m-1, 0, n-1
while top <= bot and lft <= rgt:
    for j in range(lft, rgt+1):
        ans.append(matrix[top][j])
    top += 1
    for i in range(top, bot+1):
        ans.append(matrix[i][rgt])
    rgt -= 1
    if top <= bot:
        for j in range(rgt, lft-1, -1):
            ans.append(matrix[bot][j])
        bot -= 1
    if lft <= rgt:
        for i in range(bot, top-1, -1):
            ans.append(matrix[i][lft])
        lft += 1
print(*ans)
