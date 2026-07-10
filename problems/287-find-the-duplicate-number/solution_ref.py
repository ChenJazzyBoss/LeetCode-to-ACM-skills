import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# Floyd 判圈法: 把 nums[i] 当成 "下一个节点" 指针
slow = fast = 0
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break

# 找入环点 = 重复值
slow = 0
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
print(slow)
