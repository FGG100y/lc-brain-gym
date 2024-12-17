"""5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
"""
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        def expand_around_center(left, right):
            # 从中心扩展，找到最长的回文长度
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # 回文的长度

        max_len = 0
        end, start = 0, 0
        for i in range(len(s)):
            # 奇数长度回文串
            len1 = expand_around_center(i, i)
            # 偶数长度回文串
            len2 = expand_around_center(i, i + 1)
            # 更新最大长度
            max_len = max(len1, len2)
            # 计算起点终点索引
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
            #  print(i, max_len, start, end)

        return s[start:end+1]


# 读取输入
#  s = input().strip()
s = "babad"
print(Solution().longestPalindrome(s))
#  输出："bab"
