import sys
input = lambda: sys.stdin.readline()

def solve():
    line1 = input().strip()
    nums1 = list(map(int, line1.split())) if line1 else []
    line2 = input().strip()
    nums2 = list(map(int, line2.split())) if line2 else []
    merged = sorted(nums1 + nums2)
    total = len(merged)
    if total % 2 == 1:
        print(merged[total // 2])
    else:
        print(merged[total // 2 - 1])

solve()
