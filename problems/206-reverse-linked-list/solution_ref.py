import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    if n == 0:
        return
    nums = list(map(int, input().split()))
    nums.reverse()
    print(*nums)

solve()
