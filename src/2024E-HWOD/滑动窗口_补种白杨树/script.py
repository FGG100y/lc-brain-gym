def max_continuous_trees(N, M, dead_trees, K):
    # 滑动窗口

    dead_set = set(dead_trees)

    max_continous = 0           # 用于记录区间最大长度
    dead_cnt = 0                # 用于与 K 比较
    left = 0

    # 维护 左边界，右边界索引
    for right in range(1, N+1):
        if right in dead_set:
            dead_cnt += 1

        while dead_cnt > K:         # 只能补种K棵树，亦即窗口大小固定
            left += 1               # 移动窗口左端索引
            if left in dead_set:    # 如果移动左端索引恰对应死苗
                dead_cnt -= 1       # 死苗总数要减一，亦即补种名额加一
        max_continous = max(max_continous, right - left)

    return max_continous


# 示例1
N1 = 5
M1 = 2
dead_trees1 = [2, 4]
K1 = 1
print(max_continuous_trees(N1, M1, dead_trees1, K1))  # 输出: 3

# 示例2
N2 = 10
M2 = 3
dead_trees2 = [2, 4, 7]
K2 = 1
print(max_continuous_trees(N2, M2, dead_trees2, K2))  # 输出: 6
