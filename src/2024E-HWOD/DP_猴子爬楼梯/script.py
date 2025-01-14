"""
猴子爬楼梯，一次可以爬1个台阶或者3个台阶，n个台阶有多少种爬法

与计算Fibonacci的动态规划（tabular方法）类似，基础情况不同而已。
"""
def monkey_climb_stairs(n):
    # 特殊情况处理
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2

    # 初始化 dp 数组
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 1, 2

    # 动态规划计算
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    return dp[n]

# 测试
n = 5
output = monkey_climb_stairs(n)
print(output)  # 输出 3个台阶有几种爬法

