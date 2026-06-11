import sys
input = lambda: sys.stdin.readline()

def solve():
    digits = input().strip()
    if not digits:
        return
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    results = []
    def dfs(idx, path):
        if idx == len(digits):
            results.append(''.join(path))
            return
        for ch in mapping[digits[idx]]:
            path.append(ch)
            dfs(idx + 1, path)
            path.pop()
    dfs(0, [])
    results.sort()
    for r in results:
        print(r)

solve()
