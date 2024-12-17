"""2470. 最小公倍数等k的子数组

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数
为 k 的子数组数目。

子数组 是数组中一个连续非空的元素序列。

数组的最小公倍数 是可被所有数组元素整除的最小正整数。

示例 1 ：
输入：nums = [3,6,2,7,1], k = 6
输出：4
"""
#  from math import gcd as mgcd

# 辗转相除求最大公约数(greatest common divisor)
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# 借助gcd()计算最小公倍数(least common multiple)
def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)
    #  return a * b // mgcd(a, b)


def subarrayLCM(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        curr_lcm = nums[i]
        for j in range(i, n):
            curr_lcm = lcm(curr_lcm, nums[j])

            if curr_lcm > k:
                break
            if curr_lcm == k:
                count += 1

    return count


nums = [3,6,2,7,1]
k = 6
print(subarrayLCM(nums, k))
