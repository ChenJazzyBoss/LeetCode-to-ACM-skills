import sys
input = lambda: sys.stdin.readline()

def solve():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    iv = int(input())
    if iv == 0:
        print(-1)
        return
    # 找到 A、B 中第一个等于 iv 且其后缀相同的交点值
    print(iv)

solve()
