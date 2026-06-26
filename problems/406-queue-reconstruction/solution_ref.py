import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    people = []
    for _ in range(n):
        h, k = map(int, input().split())
        people.append((h, k))
    people.sort(key=lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    for h, k in res:
        print(h, k)

solve()
