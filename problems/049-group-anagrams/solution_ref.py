import sys
from collections import defaultdict
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    strs = input().split()
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    result = []
    for key in groups:
        group = sorted(groups[key])
        result.append(group)
    result.sort(key=lambda g: g[0])
    for group in result:
        print(*group)

solve()
