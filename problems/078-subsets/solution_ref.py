import sys
input = lambda: sys.stdin.readline()

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    results = []

    def dfs(start, path):
        results.append(path[:])
        for i in range(start, n):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    results.sort(key=lambda x: (len(x), x))
    for subset in results:
        if subset:
            print(*subset)
        else:
            print()

solve()
