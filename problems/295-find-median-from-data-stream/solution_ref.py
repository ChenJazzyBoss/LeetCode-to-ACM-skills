import sys, heapq
input = lambda: sys.stdin.readline()

def solve():
    q = int(input())
    lo = []  # max-heap (存负数)
    hi = []  # min-heap
    for _ in range(q):
        parts = input().split()
        if parts[0] == 'ADDNUM':
            num = int(parts[1])
            heapq.heappush(lo, -num)
            heapq.heappush(hi, -heapq.heappop(lo))
            if len(lo) < len(hi):
                heapq.heappush(lo, -heapq.heappop(hi))
        else:
            if len(lo) > len(hi):
                print(f"{-lo[0]:.1f}")
            else:
                print(f"{(-lo[0] + hi[0]) / 2:.1f}")

solve()
