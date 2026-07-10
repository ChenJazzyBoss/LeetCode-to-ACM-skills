import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
ans = end = maxr = 0
for i in range(n - 1):
    maxr = max(maxr, i + nums[i])
    if i == end:
        ans += 1
        end = maxr
print(ans)
