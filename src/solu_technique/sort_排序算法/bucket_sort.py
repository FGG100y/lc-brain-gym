""" leetcode 347 前 K 个高频元素

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺
序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""

from collections import Counter
import heapq

# NOTE that Counter.most_common() depends on heaq.nlargest()
def topKFrequent1(nums, k):         # O(n log n)
    # 统计每个元素的频率
    count = Counter(nums)

    # 使用堆找出频率最高的k个元素
    return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

def topKFrequent2(nums, k):         # O(n log n)
    # 使用 Counter 统计频率，并通过 most_common 返回前 k 个元素
    return [item for item, _ in Counter(nums).most_common(k)]


def topKFrequent(nums, k):          # O(n)
    # 统计每个元素的频率
    counter = Counter(nums)

    # 创建频率桶，索引是频率，桶里存放的是具有该频率的元素
    freq_bucket = [[] for _ in range(len(nums) + 1)]
    for num, freq in counter.items():
        freq_bucket[freq].append(num)

    # 从频率最高的桶开始收集元素
    result = []
    for i in range(len(freq_bucket) - 1, 0, -1):
        for num in freq_bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

nums = [1,1,2,2,2,3]
k = 2
print(topKFrequent(nums, k))
print(topKFrequent1(nums, k))
print(topKFrequent2(nums, k))
