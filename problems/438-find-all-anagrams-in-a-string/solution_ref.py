import sys
from collections import Counter
input = sys.stdin.readline

s = input().strip()
p = input().strip()

m, n = len(s), len(p)
if m < n:
    print()
    exit()

need = Counter(p)
window = Counter(s[:n])
ans = []
if window == need:
    ans.append(0)

for i in range(n, m):
    window[s[i]] += 1                        # 右边进
    left = s[i - n]
    window[left] -= 1                         # 左边出
    if window[left] == 0:
        del window[left]
    if window == need:
        ans.append(i - n + 1)

print(*ans)
