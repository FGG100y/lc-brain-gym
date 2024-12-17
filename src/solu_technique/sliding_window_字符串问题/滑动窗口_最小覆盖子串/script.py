"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。



注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_cnter = Counter(t)
        w_cnter = Counter()
        required = len(t_cnter)         # 所需字符数
        formed = 0                      # 当前窗口满足添加字符数
        l, r = 0, 0                     # 左右指针

        ans = float("inf"), None, None  # 长度，左指针位置，右指针位置

        while r < len(s):
            char = s[r]
            w_cnter[char] = w_cnter.get(char, 0) + 1
            # 检查窗口字符满足条件情况
            if char in t_cnter and w_cnter[char] == t_cnter[char]:
                formed += 1
            # 当前窗口满足t中所有字符频次要求，开始缩小窗口
            while l < r and formed == required:
                # 更新答案
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                char = s[l]
                # 将s[l]移出窗口
                w_cnter[char] -= 1
                if char in t_cnter and w_cnter[char] < t_cnter[char]:
                    formed -= 1

                l += 1
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
#  输出："BANC"
