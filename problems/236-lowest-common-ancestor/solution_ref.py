import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    left=[0]*(n+1); right=[0]*(n+1); hasp=[False]*(n+1)
    for _ in range(n-1):
        parts=input().split()
        p,c,side=int(parts[0]),int(parts[1]),parts[2]
        if side=='L': left[p]=c
        else: right[p]=c
        hasp[c]=True
    root=next(i for i in range(1,n+1) if not hasp[i])
    p,q = map(int, input().split())
    parent={root:0}
    # build parent map via dfs
    st=[root]
    while st:
        u=st.pop()
        for c in (left[u],right[u]):
            if c:
                parent[c]=u
                st.append(c)
    # ancestors of p
    anc=set(); x=p
    while x:
        anc.add(x); x=parent[x]
    x=q
    while x not in anc:
        x=parent[x]
    print(x)

solve()
