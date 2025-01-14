def min_strength_difference(ratings):
    total_strength = sum(ratings)
    half_strength = total_strength // 2

    # 初始化 DP 数组
    dp = [[False] * (half_strength + 1) for _ in range(len(ratings) + 1)]

    # 基础情况：不选任何选手时，总评分为0的情况
    for i in range(len(ratings) + 1):
        dp[i][0] = True

    # 动态规划填充
    for i in range(1, len(ratings) + 1):
        for j in range(1, half_strength + 1):
            if j < ratings[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - ratings[i - 1]]

    # 寻找最接近 half_strength 的评分
    for j in range(half_strength, -1, -1):
        if dp[len(ratings)][j]:
            min_diff = abs((total_strength - j) - j)
            break

    return min_diff

# 示例输入
ratings = [5, 1, 8, 3, 4, 6, 7, 11, 9, 2]
result = min_strength_difference(ratings)
print(result)
