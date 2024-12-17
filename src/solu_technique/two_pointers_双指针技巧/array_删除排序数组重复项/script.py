"""问题描述：
给定一个排序数组，原地删除重复出现的元素，使每个元素只出现一次，并返回新的长度。

题目要求在原地删除排序数组中的重复项，即不能使用额外的数组来存储结果，删除后数组中每个元
素只出现一次，并返回新数组的长度。由于数组是排序的，因此重复的元素会连续出现。

核心思想：
我们可以使用双指针的方法：
- 一个指针 i 负责遍历整个数组。
- 另一个指针 j 用于存放不重复的元素。

只要当前元素 nums[i] 和 nums[j] 不相同，我们就将 nums[i] 赋值给 nums[j+1]，并移动指针 j。
最终，数组的前 j+1 个元素就是去重后的结果。
"""
def removeDuplicates(nums):
    if not nums:
        return 0

    # 指针 j 指向去重后的最后一个元素位置
    j = 0

    # 遍历数组
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    # 返回新数组的长度
    return j + 1


def removeDuplicates2(nums):
    if not nums:
        return 0

    j = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]     # 保留原元素
        #  print(j, i, nums)

    return j + 1


nums = [1, 1, 2, 2, 3]
#  nums = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]

#  new_length = removeDuplicates(nums)     # 这个算法会改变原数组元素，覆盖元素
#  print(new_length)                       # 输出 3
#  print(nums)                             # 输出 [1,2,3,2,3]
#  print(nums[:new_length])                # 输出 [1,2,3]

new_length = removeDuplicates2(nums)    # 这个算法不会改变原数组元素，只调整位置
print(new_length)                       # 输出 3
print(nums)                             # 输出 [1,2,3,2,1]
print(nums[:new_length])                # 输出 [1,2,3]
