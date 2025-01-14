"""
描述
找出字符串中第一个只出现一次的字符

数据范围：输入的字符串长度满足 1≤n≤1000 

输入描述：
输入一个非空字符串

输出描述：
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入：
asdfasdfo

输出：
o
"""

def first_unique_char(s):
    # 用哈希表记录每个字符的出现次数
    char_count = {}

    # 第一次遍历，统计字符出现次数
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # 第二次遍历，找到第一个出现次数为1的字符
    for char in s:
        if char_count[char] == 1:
            return char

    # 如果没有只出现一次的字符，返回 -1
    return -1


# 示例测试
s = "abaccdeff"
print(first_unique_char(s))  # 输出 'b'

# 边界情况
s = "aabbcc"
print(first_unique_char(s))  # 输出 -1

