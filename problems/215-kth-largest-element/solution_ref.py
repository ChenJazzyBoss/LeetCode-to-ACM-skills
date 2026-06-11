import sys
import heapq
input = lambda: sys.stdin.readline()

def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    # 用最小堆，维护大小为 k
    heap = nums[:k]
    heapq.heapify(heap)
    for i in range(k, n):
        if nums[i] > heap[0]:
            heapq.heapreplace(heap, nums[i])
    print(heap[0])

solve()
