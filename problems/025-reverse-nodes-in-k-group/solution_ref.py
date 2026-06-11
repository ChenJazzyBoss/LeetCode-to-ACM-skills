import sys
input = lambda: sys.stdin.readline()

def solve():
    vals = list(map(int, input().split()))
    k = int(input())
    result = []
    for i in range(0, len(vals), k):
        group = vals[i:i + k]
        if len(group) == k:
            result.extend(reversed(group))
        else:
            result.extend(group)
    print(*result)

solve()
