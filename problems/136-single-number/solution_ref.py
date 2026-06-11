import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0
    for x in nums:
        result ^= x
    print(result)

solve()
