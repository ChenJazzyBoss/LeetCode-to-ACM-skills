import sys
from collections import Counter
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()
    t = input().strip()
    need = Counter(t)
    window = Counter()
    left = 0
    valid = 0
    required = len(need)
    start, min_len = 0, len(s) + 1

    for right, ch in enumerate(s):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            valid += 1
        while valid == required:
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1
            d = s[left]
            if d in need and window[d] == need[d]:
                valid -= 1
            window[d] -= 1
            left += 1

    if min_len <= len(s):
        print(s[start:start + min_len])
    else:
        print()

solve()
