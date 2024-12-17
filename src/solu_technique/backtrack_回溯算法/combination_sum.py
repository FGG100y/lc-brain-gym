"""
eetCode 39 组合总和：给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。
"""

#回溯过程：

#维护一个当前组合（current_combination）。
#在递归中尝试加入当前的候选数字，如果加入后和没有超过目标值（target），则继续递归。
#如果组合的和刚好等于目标值，则将其加入到结果集。
#通过回溯来探索所有可能的组合，当达到条件时，将其从组合中移除，继续下一轮的尝试。

#剪枝：如果在递归过程中当前组合的和已经超过了目标值，则停止继续探索

def combination_sum(candidates, target):
    def backtrack(remaining, start, current_combination):
        if remaining == 0:
            result.append(list(current_combination))
            return
        elif remaining < 0:
            return
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(remaining - candidates[i], i, current_combination)
            current_combination.pop()
    candidates.sort()
    result = []
    backtrack(target, 0, [])
    return result
