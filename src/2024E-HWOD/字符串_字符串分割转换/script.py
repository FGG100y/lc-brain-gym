"""
字符串分割转换
问题描述
给定一个非空字符串S，它被N 个 '-' 分隔成N+1 个子串。现在给定一个正整数K，要求对S 进行如
下处理：

保留第一个子串不变。对于剩余的子串，每K 个字符组成一个新的子串，用 '-' 分隔。

对于每个新组成的子串，进行以下转换：
如果小写字母数量多于大写字母，将所有大写字母转换为小写字母。
如果大写字母数量多于小写字母，将所有小写字母转换为大写字母。
如果大小写字母数量相等，不进行转换。
请输出处理后的字符串。

输入格式
输入包含两行：
第一行为一个正整数K。
第二行为字符串S。

输出格式
输出一行，为处理后的字符串。

样例输入
3
12abc-abCABc-4aB@
样例输出
12abc-abc-ABC-4aB-@
样例解释
原始子串为 "12abc"、"abCABc"、"4aB@"。第一个子串 "12abc" 保留不变。剩余部分每 3 个字符一
组，得到 "abC"、"ABc"、"4aB"、"@"。

"abC" 中小写字母较多，转换为 "abc"。
"ABc" 中大写字母较多，转换为 "ABC"。
"4aB" 中大小写字母数量相等，保持不变。
"@" 中没有字母，保持不变。
最后用 '-' 连接所有部分，得到 "12abc-abc-ABC-4aB-@"。

样例输入
12
12abc-abCABc-4aB@
样例输出
12abc-abCABc4aB@
样例解释
原始子串为 "12abc"、"abCABc"、"4aB@"。第一个子串 "12abc" 保留不变。剩余部分作为一个整体
"abCABc4aB@"，其中大小写字母数量相等，因此不做转换。最后用 '-' 连接，得到
"12abc-abCABc4aB@"。
"""

# prefix = s.split("-")[0]
# rest = s.split("-")[1:]
# while i < len(rest) - k: chunk=rest[i+k], chunk[0].isupper() for counting upper/lower cases, etc

def process_string(K, S):
    # 按 '-' 分割字符串
    parts = S.split('-')

    # 保留第一个子串
    result = [parts[0]]
    rest = "".join(parts[1:])

    # 将子串分为每 K 个字符的组
    for i in range(1, len(rest), K):
        group = rest[i:i+K]

        # 统计大写字母和小写字母个数
        lower_count = sum(c.islower() for c in group)
        upper_count = sum(c.isupper() for c in group)

        # 根据字母数量调整大小写
        if lower_count > upper_count:
            group = group.lower()
        elif upper_count > lower_count:
            group = group.upper()

        # 将处理后的子串加入结果
        result.append(group)

    # 最终结果拼接
    return '-'.join(result)

# 输入
K = 3
S = "12abc-abCABc-4aB@"
S = "12abc-bCABc-4aB@"

# 输出结果
print(process_string(K, S))
