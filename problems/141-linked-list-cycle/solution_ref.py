import sys
input = lambda: sys.stdin.readline()

def solve():
    vals = list(map(int, input().split()))
    pos = int(input())
    n = len(vals)
    slow = fast = 0
    has_cycle = False
    if n > 0 and pos != -1:
        # 快慢指针模拟
        def nxt(i):
            return i + 1 if i + 1 < n else pos
        slow = nxt(0)
        fast = nxt(nxt(0))
        while slow != fast:
            slow = nxt(slow)
            fast = nxt(nxt(fast))
        has_cycle = True
    print("True" if has_cycle else "False")

solve()
