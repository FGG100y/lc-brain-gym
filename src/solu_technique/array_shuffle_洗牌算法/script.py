"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该
是 等可能 的。

实现 Solution class:
- Solution(int[] nums) 使用整数数组 nums 初始化对象
- int[] reset() 重设数组到它的初始状态并返回
- int[] shuffle() 返回数组随机打乱后的结果

示例 1：
输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
"""
import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums[:]  # 保存原始数组
        self.array = nums[:]     # 当前数组用于操作

    def reset(self) -> list[int]:
        # 将数组重设为原始状态
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> list[int]:
        # 使用 Fisher-Yates 洗牌算法来打乱数组
        for i in range(len(self.array) - 1, 0, -1):
            j = random.randint(0, i)  # 在 [0, i] 范围内随机选择索引
            self.array[i], self.array[j] = self.array[j], self.array[i]  # 交换元素
        return self.array


arr = [1, 2, 3]
solu = Solution(arr)
print(solu.shuffle())
print(solu.reset())
print(solu.shuffle())

