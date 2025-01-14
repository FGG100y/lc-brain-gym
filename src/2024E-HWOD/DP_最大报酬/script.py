"""
小明每周上班都会拿到自己的工作清单，工作清单内包含n 项工作，每项工作都有对应的耗时时间
（单位 h）和报酬，工作的总报酬为所有已完成工作的报酬之和。请你帮小明安排工作，保证小明在
指定的工作时间内工作收入最大化。

输入格式
第一行包含两个正整数T 和n。T 代表工作时长（单位 h），n 代表工作数量。
接下来n 行，每行包含两个整数t_i和w_i。t_i代表第i 项工作消耗的时长（单位 h），w_i代表第i
项工作的报酬。

输出格式
输出一个整数，表示小明在指定工作时长内可获得的最大报酬。

样例输入
40 3
20 10
20 20
20 5
样例输出
30
"""

def max_pay(jobs_arr, T):
    # 0/1 knapsack, DP for solution
    dp = [0] * (T + 1)

    for t_i, w_i in jobs_arr:
        # 逆序遍历 dp 数组，确保每个工作只能选一次
        for j in range(T, t_i - 1, -1):
            #  print(j, dp[j], "\tmax of", dp[j], "or", dp[j - t_i], "+", w_i)
            dp[j] = max(dp[j], dp[j - t_i] + w_i)
    return dp[T]


T, n = 40, 3
arr_raw = """
20 10
20 20
20 5
"""
arr = [map(int, line.split()) for line in arr_raw.strip("\n").splitlines()]
print(max_pay(arr, T))
