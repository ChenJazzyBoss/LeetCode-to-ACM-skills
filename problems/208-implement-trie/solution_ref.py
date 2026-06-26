import sys
input = lambda: sys.stdin.readline()

class Trie:
    def __init__(self):
        self.ch = {}
        self.end = False
    def insert(self, w):
        node = self
        for c in w:
            node = node.ch.setdefault(c, Trie())
        node.end = True
    def _find(self, w):
        node = self
        for c in w:
            if c not in node.ch:
                return None
            node = node.ch[c]
        return node
    def search(self, w):
        node = self._find(w)
        return node is not None and node.end
    def startsWith(self, w):
        return self._find(w) is not None

def solve():
    q = int(input())
    root = Trie()
    for _ in range(q):
        parts = input().split()
        op, w = parts[0], parts[1]
        if op == 'INSERT':
            root.insert(w)
        elif op == 'SEARCH':
            print('True' if root.search(w) else 'False')
        else:
            print('True' if root.startsWith(w) else 'False')

solve()
