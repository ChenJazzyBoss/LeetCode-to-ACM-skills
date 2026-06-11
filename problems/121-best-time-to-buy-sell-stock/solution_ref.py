import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    prices = list(map(int, input().split()))
    min_price = prices[0]
    max_profit = 0
    for p in prices[1:]:
        max_profit = max(max_profit, p - min_price)
        min_price = min(min_price, p)
    print(max_profit)

solve()
