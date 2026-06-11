import sys
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()
    n = len(s)
    if n == 0:
        print("")
        return
    start, max_len = 0, 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)      # 奇数长度
        expand(i, i + 1)  # 偶数长度

    print(s[start:start + max_len])

solve()
