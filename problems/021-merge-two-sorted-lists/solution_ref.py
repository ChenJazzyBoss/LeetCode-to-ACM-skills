import sys
input = lambda: sys.stdin.readline()

def solve():
    line1 = input().strip()
    line2 = input().strip()
    a = list(map(int, line1.split())) if line1 else []
    b = list(map(int, line2.split())) if line2 else []
    merged = sorted(a + b)
    print(*merged) if merged else print()

solve()
