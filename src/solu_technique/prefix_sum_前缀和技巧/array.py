"""
一维数组前缀和技巧: 前缀和技巧适用于快速、频繁地计算一个索引区间内的元素之和。

***

给定一个整数数组  nums，处理以下类型的多个查询:

计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含
left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )


示例 1：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
"""

#  from typing import List


class NumArray:

    def __init__(self, nums: list[int]):
        self.pre_sum = [0] * (len(nums) + 1)
        i = 1
        while i < len(self.pre_sum):
            self.pre_sum[i] = self.pre_sum[i - 1] + nums[i - 1]
            i += 1

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]


if __name__ == "__main__":

    # Your NumArray object will be instantiated and called as such:
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    for lt in [[0, 2], [2, 5], [0, 5]]:
        left, right = lt[0], lt[1]
        print(obj.sumRange(left, right), end=" ")
    print()

    #  [null, 1, -1, -3]
