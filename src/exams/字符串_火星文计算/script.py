# 计算符号定义
def mars_hash_ops(x, y):
    return 4 * x + 3 * y + 2
def mars_doller_ops(x, y):
    return 2 * x + y + 3

def marsian_cal(expr):

    n = len(expr)
    nums = []
    ops = []
    i = 0
    # 提取表达式中的数字和符号
    #  71#6$5#12
    while i < n:
        if expr[i].isdigit():  # valid expr check
            num = 0
            while i < n and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            nums.append(num)
        else:
            ops.append(expr[i])
            i += 1
    # 处理 # 运算
    new_nums = [nums[0]]  # 构造新表达式（列表，只剩 $ 运算符号）
    for j in range(len(ops)):
        if ops[j] == "#":
            new_nums[-1] = mars_hash_ops(new_nums[-1], nums[j+1])
        else:
            new_nums.append(nums[j+1])
    # 处理 $ 运算 （操作前一个运算符不一样）
    # new_nums 中的元素个数是 $ 运算符个数+1
    result = new_nums[0]
    for i in range(1, len(new_nums)):
        result = mars_doller_ops(result, new_nums[i])
    print(result)
    return result


expr = "7#6$5#12$2"
assert marsian_cal(expr) == mars_doller_ops(157, 2)
