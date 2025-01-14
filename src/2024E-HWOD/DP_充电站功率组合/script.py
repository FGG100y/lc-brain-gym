"""
题目描述：某个充电站，可提供 n 个充电设备，每个均有对应的输出功率。任意个充电设备组合的
输出功率总和，均构成功率集合P的一个元素。功率集合P的最优元素，表示最接近充电站最大输出功
率p_max的元素。
输入描述：
第一行充电设备数量n；
第二行每个设备输出功率；
第三行电站最大输出功率p_max.
输出：
功率集合的最优元素。
样例输入 1
4
50 20 20 60
90
样例输出 1
90
样例解释 1
当充电设备输出功率 50、20、20 组合时，其输出功率总和为 90，最接近充电站最大充电输出功率，
因此最优元素为 90。
样例输入 2
2
50 40
30
样例输出 2
0
样例解释 2
所有充电设备的输出功率组合，均大于充电站最大充电输出功率 30，此时最优元素值为 0。
"""

def max_power(n, powers, p_max):
    dp = [False] * (p_max + 1)
    dp[0] = True

    for power in powers:
        for j in range(p_max, power - 1, -1):
            dp[j] = dp[j] or dp[j - power]

    for k in range(p_max, -1, -1):
        if dp[k]:
            return k

    return 0

def optimal_power_combination(n, powers, p_max):
    # 初始化功率集合，初始时只包含0
    power_set = {0}

    # 动态更新功率集合
    for power in powers:
        # 对当前已有的功率集合元素进行扩展
        new_combinations = {x + power for x in power_set if x + power <= p_max}
        power_set.update(new_combinations)

    # 在功率集合中寻找最接近 p_max 的值
    best_power = max(power_set)

    return best_power


n = 4
p_max = 90
powers_raw = "50 20 20 60"
n = 2
p_max = 100
powers_raw = "50 60 20"
powers = list(map(int, powers_raw.split()))
print(max_power(n, powers, p_max))
print(optimal_power_combination(n, powers, p_max))
