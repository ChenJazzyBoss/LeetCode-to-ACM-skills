import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    tokens = input().split()
    it = iter(tokens)
    def build():
        v = next(it)
        if v == 'null':
            return None
        node = [int(v), None, None]  # [val, left, right]
        node[1] = build()
        node[2] = build()
        return node
    root = build()
    res = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node is None:
            continue
        res.append(node[0])
        dq.append(node[1])
        dq.append(node[2])
    print(*res)

solve()
