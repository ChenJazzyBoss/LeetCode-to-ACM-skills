import sys
input = lambda: sys.stdin.readline()

def solve():
    data = input()
    if not data.strip():
        print()
        return
    n = int(data)
    if n == 0:
        print()
        return
    nums = list(map(int, input().split()))
    nums.sort()
    print(*nums)

solve()
