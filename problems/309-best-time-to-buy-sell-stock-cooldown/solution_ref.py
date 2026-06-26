import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    prices = list(map(int, input().split()))
    hold = -prices[0]
    sold = 0
    rest = 0
    for i in range(1, n):
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold = max(prev_hold, prev_rest - prices[i])
        rest = max(prev_rest, prev_sold)
        sold = prev_hold + prices[i]
    print(max(sold, rest))

solve()
