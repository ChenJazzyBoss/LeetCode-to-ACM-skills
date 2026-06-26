import sys, heapq
input = lambda: sys.stdin.readline()

def solve():
    m = int(input())
    meetings = []
    for _ in range(m):
        s, e = map(int, input().split())
        meetings.append((s, e))
    meetings.sort()
    heap = []  # 各会议室的结束时间
    for s, e in meetings:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    print(len(heap))

solve()
