"""
题目描述
A 和 B 两个人要分苹果。A 希望按照他的计算规则得到平均分配的苹果，而 B 希望在满足 A 的条
件下获得尽可能多的苹果量。

A 的计算规则是按照二进制加法进行，并不计算进位。例如，12 + 5 = 9 （1100 + 0101 = 1001）。

B 的计算规则是正常的十进制加法，包括进位。

给定苹果的数量和每个苹果的重量，计算并满足 A 的要求的情况下，B 能获得的最大苹果总重量。
如果无法满足 A 的要求，则输出 -1。

输入描述
第一行包含一个整数 n，表示苹果的数量。

第二行包含 n 个整数，表示每个苹果的重量 w1, w2, ..., wn。

输出描述
输出一个整数，表示 B 能获得的最大苹果总重量。如果无法满足 A 的要求，则输出 -1。

示例1
输入：
3
3 5 6

输出：
11

说明：
通过二进制无进位加法，A 要求的总重量是 3 XOR 5 XOR 6 = 0，B 能获得所有的苹果，总重量为 11。
示例2
输入：
8
7258 6579 2602 6716 3050 3564 5396 1773

输出：
35165

说明：
同样按照 A 的二进制无进位规则，B 获得最大的苹果重量为 35165。
"""
# 狗屎一样的描述，根本表述不清，甚至示例还有矛盾。狗屎。2024-09-27 Fri

# XOR为0，则将最小值分配给A，剩下都是B的；否则输出-1。（不清楚这个狗屎做法为什么对题）。

# 社区靓女：意思就是 平分苹果 比如例子中(三个苹果，重量分别为：3, 5, 6) 对a的算法来说:b
# 拿到的是5+6=3个， 剩下个3，所以 a和b 是平分的。但是对b来说 他拿到的是总重量为11的两个
# 苹果。所以b能拿到的，并且满足a同学要求之后的最大重量是11.

# 终于，狗屎味散了。原来不过是LeetCode中“找唯一出现一次的数”来到此间后画的浓妆，熏着了。


def main(arr):
    xor_sum = 0
    for a in arr:
        xor_sum ^= a
    if not xor_sum:
        return sum(arr) - min(arr)
    else:
        return -1

arr_raw = "7258 6579 2602 6716 3050 3564 5396 1773"
arr_raw = "3 5 6"
arr = list(map(int, arr_raw.split()))
#  assert main(arr) == 35165
assert main(arr) == 11
