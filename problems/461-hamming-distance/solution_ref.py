import sys
input = lambda: sys.stdin.readline()

def solve():
    x, y = map(int, input().split())
    print(bin(x ^ y).count('1'))

solve()
