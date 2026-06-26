import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    tokens = input().split()
    if not tokens or tokens[0] == 'null':
        print(0); return
    # build level-order tree as [val,left,right] lists
    nodes = {}
    idx = 0
    dq = deque()
    root = [int(tokens[0]), None, None]
    nodes[0] = root
    dq.append(0)
    pos = 1
    while dq and pos < len(tokens):
        cur = dq.popleft()
        # left
        if pos < len(tokens):
            t = tokens[pos]; pos += 1
            if t != 'null':
                cid = len(nodes)
                nodes[cid] = [int(t), None, None]
                nodes[cur][1] = cid
                dq.append(cid)
        if pos < len(tokens):
            t = tokens[pos]; pos += 1
            if t != 'null':
                cid = len(nodes)
                nodes[cid] = [int(t), None, None]
                nodes[cur][2] = cid
                dq.append(cid)

    def rob(u):
        if u is None:
            return (0, 0)
        node = nodes[u]
        l = rob(node[1]); r = rob(node[2])
        take = node[0] + l[1] + r[1]
        skip = max(l) + max(r)
        return (take, skip)

    print(max(rob(0)))

solve()
