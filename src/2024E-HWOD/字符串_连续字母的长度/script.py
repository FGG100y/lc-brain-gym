"""
题目描述
给定一个字符串，只包含大写字母，求在包含同一字母的子串中，长度第 k 长的子串的长度，相同
字母只取最长的那个子串。

输入描述
第一行有一个字符串(1<长度≤100000)，只包含大写字母 第二行为 k 的值

输出描述
输出连续出现次数第 k 多的字母的次数，当第k多的字母的次数不存在时，请输出-1

示例1
输入：
AAAAHHHBBCDHHHH
3
输出：
2
说明：
同一字母连续出现的最多的是 A 和 H ，四次
第二多的是 H，3 次，但是H 已经存在 4 个连续的，故不考虑
下个最长子串是 BB，所以最终答案应该输出2.
示例2
输入：
AABAAA
2
输出：
1
说明：
同一字母连续出现的最多的是 A，三次，
第二多的还是A，两次，但A已经存在最大连续次数三次 故不考虑;
下个最长子串是 B，所以输出 1。
示例3
输入：
ABC
4
输出：
-1
说明：
只含有 3 个包含同一字母的子串，小于 k,输出 −1。
示例4
输入：
ABC
2
输出：
1
说明：
三个子串长度均为1，所以此时 k=1，k=2，k=3 这三种情况均输出 1。特此说明，避免歧义。
"""
def kth_longest_repeating_substring(s, k):
    char_map = {}

    i = 0
    while i < len(s):
        char = s[i]
        char_cnt = 1
        while i < len(s)-1 and s[i+1] == char:
            char_cnt += 1
            i += 1
        if char not in char_map:
            char_map[char] = char_cnt
        else:
            char_map[char] = max(char_map[char], char_cnt)
        i += 1
    #  print(char_map)
    result = sorted(char_map.values(), reverse=True)
    if len(result) < k:
        return -1
    return result[k-1]  # not zero base indexing



s = "AAAAHHHBBCDHHHH"
k = 3
print(kth_longest_repeating_substring(s, k))  # 3
