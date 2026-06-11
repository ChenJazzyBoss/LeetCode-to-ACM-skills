import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    candidates = sorted(set(map(int, input().split())))
    target = int(input())
    results = []

    def dfs(start, remaining, path):
        if remaining == 0:
            results.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            dfs(i, remaining - candidates[i], path)
            path.pop()

    dfs(0, target, [])
    for combo in results:
        print(*combo)

solve()
