"""力扣 645. 错误的集合
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集
合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。


示例 1：
输入：nums = [1,2,2,4]
输出：[2,3]

示例 2：
输入：nums = [1,1]
输出：[1,2]
"""

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        num_set = set(nums)  # 利用集合存储不重复的数字
        sum_of_set = sum(num_set)  # 正确的数字和
        sum_of_nums = sum(nums)  # 错误的数组和

        # 丢失的数字是： (1 + 2 + ... + n) - sum_of_set
        # 等差数列：高斯求和
        missing = (n * (n + 1)) // 2 - sum_of_set

        # 重复的数字是： sum_of_nums - sum_of_set
        duplicate = sum_of_nums - sum_of_set

        return [duplicate, missing]


nums = [1,2,2,4]
print(Solution().findErrorNums(nums))
#  输出：[2,3]
