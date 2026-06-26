import sys
from collections import OrderedDict
input = lambda: sys.stdin.readline()

def solve():
    cap = int(input())
    q = int(input())
    od = OrderedDict()
    for _ in range(q):
        parts = input().split()
        if parts[0] == 'PUT':
            k, v = int(parts[1]), int(parts[2])
            if k in od:
                od.move_to_end(k)
                od[k] = v
            else:
                if len(od) >= cap:
                    od.popitem(last=False)
                od[k] = v
        else:  # GET
            k = int(parts[1])
            if k in od:
                od.move_to_end(k)
                print(od[k])
            else:
                print(-1)

solve()
