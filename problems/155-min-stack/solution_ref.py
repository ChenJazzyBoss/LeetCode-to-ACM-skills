import sys
input = lambda: sys.stdin.readline()

def solve():
    q = int(input())
    stack = []
    min_stack = []
    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == 'push':
            x = int(parts[1])
            stack.append(x)
            if not min_stack or x <= min_stack[-1]:
                min_stack.append(x)
        elif op == 'pop':
            x = stack.pop()
            if x == min_stack[-1]:
                min_stack.pop()
        elif op == 'top':
            print(stack[-1])
        elif op == 'getMin':
            print(min_stack[-1])

solve()
