def convert_to_actual_cost(n, skip_digits):
    """根据跳过的数字计算实际费用"""
    res = 0
    base = 1
    while n > 0:
        last_digit = n % 10
        n //= 10
        # 计算实际数位，跳过定义的数字
        skipped_count = sum(1 for d in skip_digits if d <= last_digit)
        res += (last_digit - skipped_count) * base
        base *= (10 - len(skip_digits))  # 更新进制为伪进制，例如跳过两个数字时是伪8进制
    return res

# 测试用例
print(convert_to_actual_cost(5, {4}))  # 输出 5 -> 实际费用为4
print(convert_to_actual_cost(17, {4}))  # 输出 17 -> 实际费用为15
print(convert_to_actual_cost(100, {4}))  # 输出 100 -> 实际费用为81
print()
# 测试用例
print(convert_to_actual_cost(5, {4, 7}))  # 输出 5 -> 实际费用为4
print(convert_to_actual_cost(18, {4, 7}))  # 输出 18 -> 实际费用为 14 (4-5, 7-8, 14-15, 17-18)
print(convert_to_actual_cost(100, {4, 7}))  # 输出 100 -> 实际费用为 64 (4-5, 7-8, 14-15, 17-18, ...)
