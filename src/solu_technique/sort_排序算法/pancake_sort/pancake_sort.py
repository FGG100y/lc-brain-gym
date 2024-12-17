"""leetcode 969 煎饼排序
给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。

一次煎饼翻转的执行过程如下：

选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,
2,3,4] 。

以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在
10 * arr.length 范围内的有效答案都将被判断为正确。

示例 1：
输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。

示例 2：
输入：[1,2,3]
输出：[]
解释：
输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。
"""
#  from collections import deque

#  FIXME dfs not work
def pancakeSort_dfs(arr: list[int]) -> list[int]:
    pass


class Solution:
    # 记录反转操作序列
    def __init__(self):
        self.res = []

    def pancakeSort(self, arr: list[int]) -> list[int]:

        self.sort(arr, len(arr))
        return self.res

    def sort(self, cakes: list[int], n: int):
        # base case
        if 1 == n:
            return

        # 寻找最大饼的索引
        max_cake_index = cakes[:n].index(n)

        # 下面进行把最大的饼放到最后的两次翻转
        # 如果最后一个饼就是最大的, 就不需要翻转, 直接进行下次递归
        if max_cake_index != n - 1:
            # 第一次翻转, 将最大饼翻到最上面
            # 如果第一个饼本来就是最大的, 就不需要第一次翻转.
            if max_cake_index != 0:
                cakes[:max_cake_index + 1] = cakes[:max_cake_index + 1][::-1]
                self.res.append(max_cake_index + 1)

            # 第二次翻转，将最大饼翻到最下面
            cakes[:n] = cakes[:n][::-1]
            self.res.append(n)

        # 递归调用
        self.sort(cakes, n - 1)

cakes = [3, 2, 4, 1]
print(Solution().pancakeSort(cakes))
print(pancakeSort_dfs(cakes))
