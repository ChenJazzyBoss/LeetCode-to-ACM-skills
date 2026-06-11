import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    nums = list(map(int, input().split()))
    num_set = set(nums)
    max_len = 0
    for x in num_set:
        if x - 1 not in num_set:
            cur = x
            cur_len = 1
            while cur + 1 in num_set:
                cur += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
    print(max_len)

solve()
