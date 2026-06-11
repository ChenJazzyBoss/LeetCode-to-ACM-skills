import sys
input = lambda: sys.stdin.readline()

def solve():
    s = input().strip()
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                print("false")
                return
    print("true" if not stack else "false")

solve()
