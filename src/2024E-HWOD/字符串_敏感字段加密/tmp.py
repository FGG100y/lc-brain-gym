import re

def encrypt_sensitive_field(K, S):
    # 解析命令字，注意处理双引号包裹的部分
    parts = []
    i = 0
    while i < len(S):
        if S[i] == '"':  # 遇到双引号
            end_quote = S.find('"', i + 1)
            if end_quote == -1:
                return "ERROR"
            parts.append(S[i:end_quote + 1])
            i = end_quote + 1
        else:  # 普通命令字或下划线分隔
            start = i
            while i < len(S) and S[i] != '_':
                i += 1
            if start != i:
                parts.append(S[start:i])
            while i < len(S) and S[i] == '_':  # 跳过连续的下划线
                i += 1

    # 检查索引是否在范围内
    if K >= len(parts):
        return "ERROR"

    # 替换敏感字段
    parts[K] = "******"

    # 拼接处理后的命令字符串
    result = "_".join(parts)

    # 使用正则表达式处理多余的下划线，删除首尾和中间连续的下划线
    result = re.sub(r'_+', '_', result)  # 合并连续下划线
    result = result.strip('_')  # 移除首尾下划线

    return result

# 输入处理
K = 1
S = '__password__a12345678_timeout___100'
assert encrypt_sensitive_field(K, S) == "password_******_timeout_100"
K = 2
S = 'aaa_password_"a12_45678"_timeout__100_""_'
# 输出处理后的命令字符串
assert encrypt_sensitive_field(K, S) == 'aaa_password_******_timeout_100_""'

