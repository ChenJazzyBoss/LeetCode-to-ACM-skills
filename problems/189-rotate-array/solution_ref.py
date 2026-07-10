import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
k = int(input()) % n
print(*(nums[-k:] + nums[:-k]))
