import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    results = []
    used = [False] * n

    def dfs(path):
        if len(path) == n:
            results.append(path[:])
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

    dfs([])
    results.sort()
    for perm in results:
        print(*perm)

solve()
