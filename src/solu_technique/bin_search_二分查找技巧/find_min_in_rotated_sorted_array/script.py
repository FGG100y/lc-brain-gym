"""153. 寻找旋转排序数组中的最小值

    NOTE NOTE NOTE 33. 搜索旋转排序数组
    153题与33题的题目非常类似，但求解逻辑细节非常不同。

已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，
原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1],
a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次
旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

示例 2：
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 3 次得到输入数组。

示例 3：
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。


"""
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # return min(nums)    # how min() do this? one may ask. Not brute-force.
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 如果中点位置元素大于右边界，最小值在右半部分
            if nums[mid] > nums[right]:
                left = mid + 1
            # 否则，最小值在左半部分或者是在mid位置
            else:
                right = mid
        return nums[left]


nums = [4,5,6,7,1,2]
print(Solution().findMin(nums))     # O(log n)，排序后数组的二分查找才有这性能


# # how min() do this? one may ask. Not brute-force. -> pseudo_min: O(n)
def pseudo_min(*args, key=None):
    if len(args) == 1:  # 处理单个可迭代对象的情况
        iterable = args[0]
    else:  # 处理多个参数的情况
        iterable = args

    # 初始化最小值为可迭代对象中的第一个元素
    it = iter(iterable)
    min_val = next(it)

    # 遍历剩下的元素，找到最小的值
    for val in it:
        if key is None:  # 不使用 key 函数
            if val < min_val:
                min_val = val
        else:  # 使用 key 函数
            if key(val) < key(min_val):
                min_val = val

    return min_val

print(pseudo_min(nums))

