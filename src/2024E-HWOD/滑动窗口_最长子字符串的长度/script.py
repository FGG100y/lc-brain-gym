"""
题目描述
给你一个字符串 s，首尾相连成一个环形，请你在环中找出 'o' 字符出现了偶数次最长子字符串的长度。

输入描述
输入是一个小写字母组成的字符串

输出描述
输出是一个整数

备注1 ≤ s.length ≤ 500000， s 只包含小写英文字母

用例1
输入
alolobo
输出
6
"""
def longest_even_o_substring(s: str) -> int:
    n = len(s)
    s = s + s  # 模拟环形，将字符串拼接自身
    max_len = 0
    o_count = 0  # 记录当前窗口内 'o' 字符的个数
    left = 0  # 滑动窗口左边界

    for right in range(2 * n):
        # 如果遇到 'o'，更新计数器
        if s[right] == 'o':
            o_count += 1

        # 确保窗口长度不会超过原始字符串的长度
        while right - left + 1 > n:
            # 窗口收缩，移除 left 位置的字符
            if s[left] == 'o':
                o_count -= 1
            left += 1

        # 检查当前窗口中 'o' 字符是否为偶数
        if o_count % 2 == 0:
            max_len = max(max_len, right - left + 1)

    return max_len

# 示例输入
s = "alolobooo"
print(longest_even_o_substring(s))  # 输出: 8

