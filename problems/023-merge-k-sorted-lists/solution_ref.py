import sys
import heapq
input = lambda: sys.stdin.readline()

def solve():
    k = int(input())
    heap = []
    for _ in range(k):
        line = input().strip()
        if line:
            for x in map(int, line.split()):
                heapq.heappush(heap, x)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    print(*result) if result else print()

solve()
