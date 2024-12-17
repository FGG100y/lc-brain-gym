"""
描述
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输
出（按原字符串的相对位置）
本题含有多组样例输入。

数据范围：字符串长度1≤n≤200  ， 保证每组输入都至少含有一个数字

输入描述：
输入一个字符串。1<=len(字符串)<=200

输出描述：
输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输
出（中间不要输出空格）。

示例1
输入：
abcd12345ed125ss123058789
a8a72a6a5yy98y65ee1r2
复制
输出：
123058789,9
729865,2
说明：
样例一最长的数字子串为123058789，长度为9
样例二最长的数字子串有72,98,65，长度都为2
"""
import re

def find_longest_digit_substrings(s):
    # 使用正则表达式提取所有的数字子串
    digit_substrings = re.findall(r'\d+', s)

    # 找出最长的数字子串的长度
    max_len = max(len(substring) for substring in digit_substrings)

    # 找出所有与最长长度相同的子串
    longest_substrings = [substring for substring in digit_substrings if len(substring) == max_len]

    # 输出所有最长的数字子串和它们的长度
    print(f"{''.join(longest_substrings)},{max_len}")

#  # 处理多组输入
#  while True:
#      try:
#          s = input().strip()  # 读取输入
#          find_longest_digit_substrings(s)
#      except EOFError:
#          break

s_raw = """
abcd12345ed125ss123058789
a8a72a6a5yy98y65ee1r2
"""
seqs = s_raw.strip("\n").splitlines()
for s in seqs:
    find_longest_digit_substrings(s)

