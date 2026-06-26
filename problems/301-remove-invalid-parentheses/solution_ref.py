import sys
from collections import deque
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()

    def valid(t):
        bal = 0
        for c in t:
            if c == '(':
                bal += 1
            elif c == ')':
                bal -= 1
                if bal < 0:
                    return False
        return bal == 0

    visited = {s}
    dq = deque([s])
    found = []
    done = False
    while dq and not done:
        for _ in range(len(dq)):
            t = dq.popleft()
            if valid(t):
                found.append(t)
                done = True
            if done:
                continue
            for i in range(len(t)):
                if t[i] in '()':
                    nt = t[:i] + t[i+1:]
                    if nt not in visited:
                        visited.add(nt)
                        dq.append(nt)
    found = sorted(set(found))
    for r in found:
        print(r)
    if not found:
        print()

solve()
