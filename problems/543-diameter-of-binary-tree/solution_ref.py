import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    tokens = input().split()
    if not tokens or tokens[0] == 'null':
        print(0); return
    nodes = {}
    nodes[0] = [int(tokens[0]), None, None]
    dq = deque([0]); pos = 1
    while dq and pos < len(tokens):
        cur = dq.popleft()
        for slot in (1, 2):
            if pos < len(tokens):
                t = tokens[pos]; pos += 1
                if t != 'null':
                    cid = len(nodes)
                    nodes[cid] = [int(t), None, None]
                    nodes[cur][slot] = cid
                    dq.append(cid)
    ans = 0
    def depth(u):
        nonlocal ans
        if u is None:
            return 0
        node = nodes[u]
        l = depth(node[1])
        r = depth(node[2])
        ans = max(ans, l + r)
        return max(l, r) + 1
    depth(0)
    print(ans)

solve()
