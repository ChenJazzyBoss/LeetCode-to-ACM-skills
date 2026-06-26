import sys
from collections import Counter
input = lambda: sys.stdin.readline()

def solve():
    line = input().split()
    tasks = []
    for tok in line:
        tasks.extend(list(tok))
    n = int(input())
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for v in counts.values() if v == max_freq)
    ans = max((max_freq - 1) * (n + 1) + max_count, len(tasks))
    print(ans)

solve()
