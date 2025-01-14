import re


def encrypt_sensitive_field(s, k):
    # 解析命令字为单独部分，
    # 替换敏感字段，
    # 最后再重新合并所有单独部分，并用正则表达式删除多余“_”
    parts = []

    i = 0
    while i < len(s):
        # 处理双引号
        if s[i] == '"':  # 有始必有终
            end_quote_idx = s.find('"', i+1)
            if end_quote_idx == "-1":   # 未找到
                return "ERROR"
            parts.append(s[i:end_quote_idx+1])
            i = end_quote_idx + 1       # 跳过命令字
        else:
            start = i
            while i < len(s) and s[i] != "_":
                i += 1
            if start != i:
                parts.append(s[start:i])
            while i < len(s) and s[i] == "_":
                i += 1
    if k >= len(s):
        return "ERROR"

    parts[k] = "******"

    result = "_".join(parts)

    # 处理多余下划线
    result = re.sub(r"_+", "_", result)
    result = result.strip("-")

    return result

# 输入处理
k = 1
s = '__password__a12345678_timeout___100'
assert encrypt_sensitive_field(s, k) == "password_******_timeout_100"
k = 2
s = 'aaa_password_"a12_45678"_timeout__100_""_'
# 输出处理后的命令字符串
assert encrypt_sensitive_field(s, k) == 'aaa_password_******_timeout_100_""'

