"""差分技巧
和前缀和（prefix_sum）思想非常类似的算法技巧「差分数组」，差分数组的主要适用场景是频繁对
原始数组的某个区间的元素进行增减。

比如说，我给你输入一个数组 nums，然后又要求给区间 nums[2..6] 全部加 1，再给 nums[3..9]
全部减 3，再给 nums[0..4] 全部加 2，再给...

一通操作猛如虎，然后问你，最后 nums 数组的值是什么？
"""


class Difference:
    def __init__(self, nums):
        # 差分数组：diff[i] = nums[i] - nums[i-1]
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def get_result(self):
        nums = [0] * len(self.diff)
        nums[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            nums[i] = nums[i - 1] + self.diff[i]
        return nums

    # 区间增减
    def increament(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val


#  leetcode 1109. 航班预订统计
#  这里有 n 个航班，它们分别从 1 到 n 进行编号。
#  有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi]
#  意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座
#  位。请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
#
#  示例 1：
#  输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
#  输出：[10,55,45,25,25]
#  解释：
#  航班编号        1   2   3   4   5
#  预订记录 1 ：   10  10
#  预订记录 2 ：       20  20
#  预订记录 3 ：       25  25  25  25
#  总座位数：      10  55  45  25  25
#  因此，answer = [10,55,45,25,25]
#
#  示例 2：
#  输入：bookings = [[1,2,10],[2,2,15]], n = 2
#  输出：[10,25]
#  解释：
#  航班编号        1   2
#  预订记录 1 ：   10  10
#  预订记录 2 ：       15
#  总座位数：      10  25
#  因此，answer = [10,25]

def total_bookings(n, bookings):
    nums = [0] * n
    df = Difference(nums)
    for arr in bookings:
        i = arr[0] - 1  # 航班编号从1开始，而数组从0开始
        j = arr[1] - 1  # 航班编号从1开始，而数组从0开始
        val = arr[2]
        df.increament(i, j, val)
    #  print(df.diff[0])
    #  breakpoint()

    return df.get_result()


n = 5
bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(total_bookings(n, bookings))
assert total_bookings(n, bookings) == [10,55,45,25,25]


# 类似题目：第 1094 题「拼车」；第 370 题「区间加法」
