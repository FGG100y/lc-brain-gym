"""最左侧冗余覆盖子串
问题描述
给定两个字符串s1 和s2 和正整数k，其中s1 长度为n1，s2 长度为n2，在s2 中选一个子串，满足：

- 该子串长度为n1+k
- 该子串中包含s1 中全部字母，该子串每个字母出现次数不小于s1 中对应的字母

我们称s2 以长度k 冗余覆盖s1，给定s1，s2，k，求最左侧的s2 以长度k 冗余覆盖s1 的子串的首个
元素的下标，如果没有返回 -1。

输入格式
输入三行：
第一行为字符串s1
第二行为字符串s2
第三行为整数k

s1 和s2 只包含小写字母。

输出格式
输出一个整数，表示最左侧的s2 以长度k 冗余覆盖s1 的子串首个元素下标，如果没有返回 -1。

样例输入
ab
aabcd
1
样例输出
0
"""

from collections import Counter

def find_leftmost_cover(s1, s2, k):
    n1 = len(s1)
    n2 = len(s2)
    win_size = n1 + k
    if n2 < win_size:
        return -1

    s1_cnter = Counter(s1)
    win_cnter = Counter()

    # init win_cnter
    win_cnter = Counter(s2[:win_size])

    # 比较字符频次
    def is_valid():
        for char, cnt in s1_cnter.items():
            if win_cnter[char] < cnt:
                return False
        return True

    if is_valid():
        return 0

    # 开始滑动窗口
    for i in range(1, n2 - win_size + 1):
        # 溢出窗口最左侧字符
        win_cnter[s2[i-1]] -= 1
        if win_cnter[s2[i-1]] == 0:
            del win_cnter[s2[i-1]]
        # 加入窗口最右侧字符
        win_cnter[s2[i + win_size - 1]] += 1

        # 检查当前窗口
        if is_valid():
            return i

    return -1



#  def find_init_index(s1, s2, k):  # 60分钟内无法解决:(
#      s1_cnter = Counter(s1)
#      win_size = len(s1) + k
#      left = 0
#
#      for right in range(len(s2)):
#          if left < right and right - left + 1 > win_size:
#              win_chars = s2[left:right]
#              win_cnter = Counter(win_chars)
#              for char, cnt in s1_cnter.items():
#                  if win_cnter[char] < cnt:
#                      left += 1
#                      break
#          return left
#
#      return -1


s1 = "ab"
s2 = "taabcd"
k = 1
print(find_leftmost_cover(s1, s2, k))  # 1
