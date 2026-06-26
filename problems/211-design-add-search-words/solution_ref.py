import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline()

class Node:
    __slots__ = ('ch', 'end')
    def __init__(self):
        self.ch = {}
        self.end = False

def solve():
    q = int(input())
    root = Node()
    for _ in range(q):
        parts = input().split()
        op, w = parts[0], parts[1]
        if op == 'ADD':
            node = root
            for c in w:
                node = node.ch.setdefault(c, Node())
            node.end = True
        else:
            def dfs(i, node):
                for j in range(i, len(w)):
                    c = w[j]
                    if c == '.':
                        return any(dfs(j+1, nxt) for nxt in node.ch.values())
                    if c not in node.ch:
                        return False
                    node = node.ch[c]
                return node.end
            print('True' if dfs(0, root) else 'False')

solve()
