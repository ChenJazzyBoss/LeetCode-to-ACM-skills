import sys
from collections import Counter
import heapq
input = lambda: sys.stdin.readline()

def solve():
    nk = input().split()
    n, k = int(nk[0]), int(nk[1])
    nums = list(map(int, input().split()))
    cnt = Counter(nums)
    # 取频率前 k
    top = heapq.nlargest(k, cnt.items(), key=lambda x: x[1])
    res = sorted(x[0] for x in top)
    print(*res)

solve()
