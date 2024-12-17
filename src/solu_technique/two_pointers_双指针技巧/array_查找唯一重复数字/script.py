"""
问题描述：给定一个包含 n + 1 个整数的数组，数字范围在 1 到 n 之间，其中有一个重复的数。
找出这个重复的数。

"""
#  参考：力扣 645. 错误的集合
def findDuplicate2(nums):
    nums_sum = sum(nums)
    sets_sum = sum(set(nums))
    return nums_sum - sets_sum

# 参考：力扣 LCR 022. 环形链表 II （单链表找出环的入口）
def findDuplicate(nums):
    # Step 1: 初始化慢指针和快指针
    slow = nums[0]
    fast = nums[0]

    # Step 2: 快慢指针移动直到相遇
    while True:
        slow = nums[slow]       # 慢指针每次走一步
        fast = nums[nums[fast]] # 快指针每次走两步
        if slow == fast:
            break

    # Step 3: 重置一个指针到起点，寻找环的入口
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # 返回重复的数字
    return slow


nums = list(map(int, "1 2 4 3 2".split()))
nums = list(map(int, "1 5 7 7 8 6 4 3 2".split()))
nums = list(map(int, "1 5 7 1 6 4 3 2".split()))
print(findDuplicate(nums))
print(findDuplicate2(nums))
