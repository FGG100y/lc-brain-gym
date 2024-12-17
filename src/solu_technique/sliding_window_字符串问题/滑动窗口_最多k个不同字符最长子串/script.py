"""
给你一个字符串 s 和一个整数 k ，请你找出至多包含 k 个不同字符的最长子串，并返回该子串的
长度。

示例 1：
输入：s = "eceba", k = 2
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。

示例 2：
输入：s = "aa", k = 1
输出：2
解释：满足题目要求的子串是 "aa" ，长度为 2 。
"""


def longest_substring(s, k):
    char_map = dict()
    max_len = 0
    left = 0

    # 01 窗口内：最多k个不同字符
    # 02 满足条件的最长子串
    # 03 返回其长度
    for right in range(len(s)):
        # 使用字典记录已出现字符
        # 如果窗口碰上新字符，且窗口内字符种类超过k，缩小窗口直到符合约束
        # 移动左指针
        # 更新最长子串长度
        if s[right] in char_map:
            char_map[s[right]] += 1
        else:
            char_map[s[right]] = 1

        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len



s = "eceba"
k = 2
assert longest_substring(s, k) == 3

s = "aa"
k = 1
assert longest_substring(s, k) == 2

