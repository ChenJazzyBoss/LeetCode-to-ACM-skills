import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    a = list(map(int, input().split())) if n > 0 else []
    m = int(input())
    b = list(map(int, input().split())) if m > 0 else []
    i = carry = 0
    result = []
    while i < len(a) or i < len(b) or carry:
        s = carry
        if i < len(a):
            s += a[i]
        if i < len(b):
            s += b[i]
        result.append(s % 10)
        carry = s // 10
        i += 1
    print(*result)

solve()
