import sys
from collections import deque
input = lambda: sys.stdin.readline()

def build(tokens):
    if not tokens or tokens[0] == 'null':
        return {}, None
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
    return nodes, 0

def solve():
    t1 = input().split()
    t2 = input().split()
    a_nodes, ar = build(t1)
    b_nodes, br = build(t2)

    def amerge(ai, bi):
        if ai is None and bi is None:
            return None
        if ai is None:
            node = b_nodes[bi]
            return [node[0], amerge(None, node[1]), amerge(None, node[2])]
        if bi is None:
            node = a_nodes[ai]
            return [node[0], amerge(node[1], None), amerge(node[2], None)]
        na, nb = a_nodes[ai], b_nodes[bi]
        return [na[0] + nb[0], amerge(na[1], nb[1]), amerge(na[2], nb[2])]

    root = amerge(ar, br)
    res = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node is None:
            res.append('null'); continue
        res.append(str(node[0]))
        dq.append(node[1]); dq.append(node[2])
    while res and res[-1] == 'null':
        res.pop()
    print(*res)

solve()
