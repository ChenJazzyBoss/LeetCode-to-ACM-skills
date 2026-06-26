import sys
input = lambda: sys.stdin.readline()

def solve():
    vals = list(map(int, input().split()))
    pos = int(input())
    n = len(vals)
    if n == 0 or pos == -1:
        print(-1)
        return
    # pos 即为入环点（题目定义尾连到 pos）
    print(pos)

solve()
