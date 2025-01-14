"""增强的strstr
问题描述
C 语言中有一个库函数 char *strstr(const char *haystack, const char *needle)，用于在字符
串 haystack 中查找第一次出现字符串 needle 的位置。现在需要实现一个 strstr 的增强函数，支
持使用带可选段的字符串进行模糊查询。

可选段使用 "[]" 标识，表示该位置可以是可选段中的任意一个字符。例如，"a[bc]" 可以匹配
"ab" 或 "ac"。

输入格式
输入包含两个字符串，分别是源字符串和目标字符串，以空格分隔。

输出格式
输出一个整数，表示匹配子字符串在源字符串中的起始位置（从 0 开始计数）。如果没有匹配，则
输出 -1。

样例输入
abcd b[cd]
样例输出
1
样例解释
目标字符串 "b[cd]" 可以匹配 "bc" 或 "bd"。在源字符串 "abcd" 中，"bc" 子字符串的起始位置
是 1。

数据范围
源字符串中不包含 '[]'。
目标字符串中的 '[]' 成对出现，且不会嵌套。
输入的字符串长度在[1,100] 之间。
"""

def enhanced_strstr(haystack, needle):
    # 解析带可选段的目标字符串，生成匹配规则
    def parse_pattern(needle):
        pattern = []
        i = 0
        while i < len(needle):
            if needle[i] == '[':
                j = i + 1
                while j < len(needle) and needle[j] != ']':
                    j += 1
                # 提取可选段的字符集合
                pattern.append(set(needle[i+1:j]))
                i = j + 1
            else:
                pattern.append(needle[i])
                i += 1
        return pattern

    # 判断源字符串的一段是否匹配解析后的目标字符串
    def matches(haystack, pattern, start):
        for i in range(len(pattern)):
            if isinstance(pattern[i], set):
                # 匹配可选段
                if haystack[start + i] not in pattern[i]:
                    return False
            else:
                # 匹配普通字符
                if haystack[start + i] != pattern[i]:
                    return False
        return True

    # 解析目标字符串
    pattern = parse_pattern(needle)
    n = len(haystack)
    m = len(pattern)

    # 滑动窗口检查匹配
    for i in range(n - m + 1):
        if matches(haystack, pattern, i):
            return i

    return -1


haystack = "abcd"
needle = "b[cd]"
print(enhanced_strstr(haystack, needle))
