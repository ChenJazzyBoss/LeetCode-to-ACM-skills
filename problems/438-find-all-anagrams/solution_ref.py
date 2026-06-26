import sys
from collections import Counter
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()
    p = input().strip()
    ns, np = len(s), len(p)
    if ns < np:
        print(); return
    pc = Counter(p)
    wc = Counter(s[:np])
    res = []
    if wc == pc:
        res.append(0)
    for i in range(np, ns):
        wc[s[i]] += 1
        wc[s[i - np]] -= 1
        if wc[s[i - np]] == 0:
            del wc[s[i - np]]
        if wc == pc:
            res.append(i - np + 1)
    print(*res) if res else print()

solve()
