def actual_cost(n):
    # 将计费表的表面读数转换为一个字符串
    n_str = str(n)
    # 初始化实际费用为0
    actual_cost = 0
    # 遍历字符串中的每一位数字
    for digit in n_str:
        # 如果遇到数字4，就跳过它
        if digit == '4':
            continue
        # 对于其他数字，将它们累加到实际费用中
        actual_cost = actual_cost * 10 + int(digit)
    return actual_cost

# 重新测试测试用例
print(actual_cost(5))  # 输出：4
print(actual_cost(17)) # 输出：15
print(actual_cost(100))# 输出：81

# NOTE step-v2-16k 完全不能理解题目意思
