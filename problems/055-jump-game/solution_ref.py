import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            print("false")
            return
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            print("true")
            return
    print("true")

solve()
