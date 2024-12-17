""" 34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组
中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""

def search_range(nums, target):

    # 查找第一个位置
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # nums[mid]是target，但是不能直接返回，
                #  而是判断mid-1位置是否还是target，
                #       是，则right指针继续向左，
                #       否，则mid已经指向第一个目标值位置，返回mid
                if mid == 0 or nums[mid-1] != target:
                    return mid
                right = mid - 1
        return -1

    # 查找最后一个位置
    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # nums[mid]是target，但是不能直接返回，
                #  而是判断mid+1位置是否还是target，
                #       是，则left指针继续向右，
                #       否，则mid已经指向最后一个目标值位置，返回mid
                #  print(f"{left=}, {mid=}, {nums[mid+1]=}")
                if mid == len(nums)-1 or nums[mid+1] != target:
                    return mid
                left = mid + 1
        return -1

    # 返回查询结果
    first = find_first(nums, target)
    if first == -1:
        return [-1, -1]
    last = find_last(nums, target)
    return [first, last]

nums = [5,7,7,8,8,9,10]
target = 8
print(search_range(nums, target))
