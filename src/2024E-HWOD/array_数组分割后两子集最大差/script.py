"""
题目描述
给定一个由若干整数组成的数组nums ，可以在数组内的任意位置进行分割，将该数组分割成两个非
空子数组(即左数组和右数组)，分别对子数组求和得到两个值.计算这两个值的差值，请输出所有分
割方案中，差值最大的值。
输入描述
第一行输入数组Q中元素个数n，1< n < 100000
第二行输入数字序列，以空格进行分隔，数字取值为4字节整数
输出描述
输出差值的最大取值
示例1
输入：
6
1 -2 3 4 -9 7
输出：
10
"""


def max_diff(nums):
    # 遍历所有分割位置，计算子数组之差
    total_sum = sum(nums)
    left_sum = 0
    max_diff = float("-inf")

    for i in range(len(nums) - 1):  # 保证非空子集，不遍历到最后一个元素
        left_sum += nums[i]
        right_sum = total_sum - left_sum
        max_diff = max(max_diff, abs(left_sum - right_sum))

    return max_diff


nums_raw = "1 -2 3 4 -9 7"
nums = list(map(int, nums_raw.split()))
print(max_diff(nums))
