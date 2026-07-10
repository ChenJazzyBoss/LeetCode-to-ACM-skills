import sys
input = sys.stdin.readline
s = input().strip()
ans = []
def dfs(start, path):
    if start == len(s):
        ans.append(path[:])
        return
    for j in range(start+1, len(s)+1):
        sub = s[start:j]
        if sub == sub[::-1]:
            path.append(sub)
            dfs(j, path)
            path.pop()
dfs(0, [])
for parts in sorted(ans):
    print(*parts)
