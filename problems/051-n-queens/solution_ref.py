import sys
input = sys.stdin.readline
n = int(input())
ans = []
def solve(row, cols, diag1, diag2, board):
    if row == n:
        ans.append([''.join(r) for r in board])
        return
    for c in range(n):
        if c in cols or (row-c) in diag1 or (row+c) in diag2:
            continue
        board[row][c] = 'Q'
        solve(row+1, cols|{c}, diag1|{row-c}, diag2|{row+c}, board)
        board[row][c] = '.'
solve(0, set(), set(), set(), [['.']*n for _ in range(n)])
for sol in ans:
    for row in sol:
        print(row)
    print()
