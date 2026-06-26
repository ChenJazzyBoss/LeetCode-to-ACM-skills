import sys
sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
input = lambda: sys.stdin.readline()

def solve():
    target = int(input())
    tokens = input().split()
    if not tokens or tokens[0] == 'null':
        print(0); return
    nodes = {}
    root = [int(tokens[0]), None, None]
    nodes[0] = root
    dq = deque([0]); pos = 1
    while dq and pos < len(tokens):
        cur = dq.popleft()
        if pos < len(tokens):
            t = tokens[pos]; pos += 1
            if t != 'null':
                cid = len(nodes); nodes[cid] = [int(t), None, None]
                nodes[cur][1] = cid; dq.append(cid)
        if pos < len(tokens):
            t = tokens[pos]; pos += 1
            if t != 'null':
                cid = len(nodes); nodes[cid] = [int(t), None, None]
                nodes[cur][2] = cid; dq.append(cid)

    count = 0
    prefix = defaultdict(int)
    prefix[0] = 1

    def dfs(u, cur_sum):
        nonlocal count
        if u is None:
            return
        node = nodes[u]
        cur_sum += node[0]
        count += prefix[cur_sum - target]
        prefix[cur_sum] += 1
        dfs(node[1], cur_sum)
        dfs(node[2], cur_sum)
        prefix[cur_sum] -= 1

    dfs(0, 0)
    print(count)

solve()
