import sys
input = sys.stdin.readline
s = input().strip()
last = {c: i for i, c in enumerate(s)}
ans = []
start = end = 0
for i, c in enumerate(s):
    end = max(end, last[c])
    if i == end:
        ans.append(end - start + 1)
        start = i + 1
print(*ans)
