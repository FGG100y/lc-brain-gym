"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的
那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

变体：有多个答案，请将它们全部找出。
"""

def twoSumAllPairs(nums, target):
    # 创建一个哈希表用于存储数值及其对应下标
    num_to_index = {}
    results = []

    for index, num in enumerate(nums):
        # 计算补数
        complement = target - num

        # 检查补数是否在哈希表中
        if complement in num_to_index:
            # 找到所有与补数匹配的下标
            for comp_index in num_to_index[complement]:
                results.append([comp_index, index])

        # 将当前数及其下标存入哈希表
        if num not in num_to_index:
            num_to_index[num] = []
        num_to_index[num].append(index)

    return results


nums = [1, 2, 3, 2, 4, 3]
target = 5
result = twoSumAllPairs(nums, target)
print(sorted(result))
#  [[0, 4], [1, 2], [1, 5], [2, 3], [3, 5]]
