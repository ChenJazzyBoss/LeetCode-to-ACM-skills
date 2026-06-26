import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    if n == 0:
        print()
        return
    left = [0]*(n+1); right=[0]*(n+1); hasp=[False]*(n+1)
    for _ in range(n-1):
        parts = input().split()
        p,c,side = int(parts[0]),int(parts[1]),parts[2]
        if side=='L': left[p]=c
        else: right[p]=c
        hasp[c]=True
    root = next(i for i in range(1,n+1) if not hasp[i])
    # 翻转即左右孩子互换
    res=[]
    dq=deque([root])
    while dq:
        u=dq.popleft(); res.append(u)
        lc,rc = right[u], left[u]  # 互换
        if lc: dq.append(lc)
        if rc: dq.append(rc)
    print(*res)

solve()
