# ============ ACM Python 快速读入模板 ============
# 适用：数据量很大（>10^5），input() 可能超时
#
# 原理：一次性读取全部输入，手动解析
#
# 输入格式：任意，按需取用

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    def next_int():
        nonlocal idx
        val = int(data[idx])
        idx += 1
        return val

    # ----- 读取输入 -----
    n = next_int()
    nums = [next_int() for _ in range(n)]

    # ----- TODO: 你的逻辑 -----

    ans = sum(nums)
    sys.stdout.write(str(ans))

main()
