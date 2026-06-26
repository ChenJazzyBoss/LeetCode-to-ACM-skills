import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    t = list(map(int, input().split()))
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and t[stack[-1]] < t[i]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    print(*res)

solve()
