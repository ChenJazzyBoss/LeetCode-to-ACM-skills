import sys
input = lambda: sys.stdin.readline()

def solve():
    vals = list(map(int, input().split()))
    n = int(input())
    k = len(vals)
    idx = k - n
    result = vals[:idx] + vals[idx + 1:]
    print(*result) if result else print()

solve()
