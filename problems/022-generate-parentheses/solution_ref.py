import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    results = []
    def dfs(left, right, path):
        if len(path) == 2 * n:
            results.append(''.join(path))
            return
        if left < n:
            path.append('(')
            dfs(left + 1, right, path)
            path.pop()
        if right < left:
            path.append(')')
            dfs(left, right + 1, path)
            path.pop()
    dfs(0, 0, [])
    results.sort()
    for r in results:
        print(r)

solve()
