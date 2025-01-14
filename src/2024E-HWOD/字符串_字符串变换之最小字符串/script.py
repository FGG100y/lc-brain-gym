"""符串变换最小字符串
问题描述
给定一个由小写字母组成的字符串s，你可以最多进行一次变换操作。变换操作的规则是：交换字符
串中任意两个不同位置的字符。请返回经过变换后能得到的字典序最小的字符串。

输入格式
输入一行，包含一个由小写字母组成的字符串s。

输出格式
输出一行，表示经过最多一次变换后得到的字典序最小的字符串。

样例输入
abcdef
样例输出
abcdef
样例解释
字符串 "abcdef" 已经是字典序最小的，不需要进行任何交换操作。

样例输入
bcdefa
样例输出
acdefb
样例解释
将 'a' 和 'b' 交换位置，可以得到字典序最小的字符串 "acdefb"。
"""
def smallest_lexicographical_string(s: str) -> str:
    # 将字符串转换为字符列表，方便交换操作
    s_list = list(s)
    n = len(s_list)

    # 遍历每个字符，查找第一个非最小字符的位置
    for i in range(n):
        # 找到当前字符后面比它小的最小字符
        min_char_index = i
        for j in range(i + 1, n):
            if s_list[j] < s_list[min_char_index]:
                min_char_index = j

        # 如果找到了比当前字符小的字符，则交换并返回结果
        if s_list[min_char_index] < s_list[i]:
            s_list[i], s_list[min_char_index] = s_list[min_char_index], s_list[i]
            return ''.join(s_list)

    # 如果没有找到可以交换的情况，直接返回原字符串
    return s

# 示例输入
s = "abcdee"
s = "bcfede"
s = "bcedea"
print(smallest_lexicographical_string(s))  # 输出: "bcdefe"

