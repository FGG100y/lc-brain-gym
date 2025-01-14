def actual_fee(N):
    result = 0
    base = 1
    while N > 0:
        last_digit = N % 10
        N //= 10
        if last_digit > 4:
            last_digit -= 1
        result += last_digit * base
        base *= 9  # 每个位置是“伪9进制”
    return result

# 测试用例1
print(actual_fee(5))    # 输出 4

# 测试用例2
print(actual_fee(17))   # 输出 15

# 测试用例3
print(actual_fee(100))  # 输出 81
