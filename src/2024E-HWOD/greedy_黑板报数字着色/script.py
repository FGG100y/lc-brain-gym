"""
黑板上已经写了N个正整数，同学们需要给这每个数分别上一种颜色。为了让黑板报既美观又有学习
意义，老师要求同种颜色的所有数都可以被这种颜色中最小的那个数整除。现在请你帮帮小朋友们，
算算至少需要多少种颜色才能给这N个数进行上色。

输入描述:
第一行有一个正整数N，其中1<=N<=100。
第二行有个N个int型整数(保证输入数据在[1,100]范围内)，表示黑板上各个正整数的值。

输出描述:
输出只有一个整数，为最少需要的颜色种数。

示例1:
输入
3
2 4 6
输出
1
"""
def min_colors(nums):
    # 贪心策略，
    # 排序数组后从最小整数开始分组（能被其整除的为一组）
    # 每增加一组，则需要多一种颜色进行着色
    nums.sort()
    color_cnt = 0
    colored = [False] * len(nums)               # 初始化数组中数字着色状态

    for i in range(len(nums)):
        if not colored[i]:                      # 如果当前数字未着色
            color_cnt += 1                      # 计数：增加一种颜色
            for j in range(i, len(nums)):       # 从当前位置开始的数组范围
                if nums[j] % nums[i] == 0:      # 找到可以被当前数字整除的
                    colored[j] = True           # 给它标记上“已着色”

    return color_cnt




nums_raw = "2 4 6 3 9 14"
nums = list(map(int, nums_raw.split()))
assert min_colors(nums) == 2
