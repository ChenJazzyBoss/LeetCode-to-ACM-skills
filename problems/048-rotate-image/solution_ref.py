import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    # 转置 + 翻转每行
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    for row in matrix:
        print(*row)

solve()
