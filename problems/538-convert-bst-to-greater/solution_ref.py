import sys
sys.setrecursionlimit(10000)
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    tokens = input().split()
    if not tokens or tokens[0] == 'null':
        print(); return
    # build tree as list of [val, left_idx, right_idx]; index in list
    nodes = [[int(tokens[0]), None, None]]
    dq = deque([0]); pos = 1
    child_of = {}  # node_idx -> dict slot->token position
    # record the slot token positions so we can replay output shape
    shape = [tokens[0]]  # output aligned to input token positions
    while dq and pos < len(tokens):
        cur = dq.popleft()
        for slot in (1, 2):
            if pos < len(tokens):
                t = tokens[pos]; pos += 1
                if t == 'null':
                    pass
                else:
                    cid = len(nodes)
                    nodes.append([int(t), None, None])
                    nodes[cur][slot] = cid
                    dq.append(cid)
    # reverse in-order accumulate
    total = 0
    def dfs(u):
        nonlocal total
        if u is None:
            return
        dfs(nodes[u][2])
        total += nodes[u][0]
        nodes[u][0] = total
        dfs(nodes[u][1])
    dfs(0)
    # replay output shape matching input token positions
    out = []
    dq2 = deque([0]); p = 0
    out.append(str(nodes[0][0])); p = 1
    while dq2 and p < len(tokens):
        cur = dq2.popleft()
        for slot in (1, 2):
            if p < len(tokens):
                t = tokens[p]; p += 1
                if t == 'null':
                    out.append('null')
                else:
                    child = nodes[cur][slot]
                    dq2.append(child)
                    out.append(str(nodes[child][0]))
    # strip trailing nulls
    while out and out[-1] == 'null':
        out.pop()
    print(*out)

solve()
