""" LeetCode 215. 数组中的第K个最大元素

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
"""
import heapq
import random


class Solution:     # 通过所有测试用例
    def findKthLargest(self, nums, k):
       min_heap = []

       for num in nums:
           heapq.heappush(min_heap, num)
           if len(min_heap) > k:
               heapq.heappop(min_heap)

       return min_heap[0]  # 堆顶元素是第 k 个最大的元素


class Solution2:    # 测试用例中存在大量重复值时，运行超时
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def quickselect(nums, left, right, k):
            if left == right:  # 只有一个元素
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_value = nums[pivot_index]

            # 移动基准到数组末尾
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            for i in range(left, right):
                if nums[i] > pivot_value:  # 找第 k 个最大元素
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 移动基准回正确的位置
            nums[store_index], nums[right] = nums[right], nums[store_index]

            if store_index == k - 1:
                return nums[store_index]
            elif store_index < k - 1:
                return quickselect(nums, store_index + 1, right, k)
            else:
                return quickselect(nums, left, store_index - 1, k)

        return quickselect(nums, 0, len(nums) - 1, k)
