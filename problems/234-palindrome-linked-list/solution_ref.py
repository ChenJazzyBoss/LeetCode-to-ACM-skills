import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    print('True' if nums == nums[::-1] else 'False')

solve()
