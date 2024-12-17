"""leetcode 78:

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""

#递归构造：从空集开始，每次递归时选择当前元素是否加入子集。
#回溯法：每次递归进入下一层时，需要保存当前选择，并在递归结束后进行回溯。
#终止条件：递归到数组的末尾时，将当前子集加入结果集中。

def subsets(nums):
    def backtrack(start, current_subset):
        result.append(list(current_subset))
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i+1, current_subset)
            current_subset.pop()
    result = []
    backtrack(0, [])
    return result
