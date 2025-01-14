"""
题目描述：喊7游戏。喊7是一个传统的聚会游戏，N个人围成一圈，按顺时针从1到N编号。从编号为1
的人开始喊数（从1开始喊），下一个人喊的数字为上一个人的数字加1，但是当要喊出来的数字是7
的倍数或者数字本身含有7的话，不能把这个数字直接喊出来，而是喊”过“替代。假定玩这个游戏的N
个人都没有失误（都在正确时机喊了”过“），当喊到数字K时，可以统计出每个人喊”过“的次数。现
给定一个长度为N的数组，存储了大乱了顺序的每个人喊”过“的次数，请把它还原成正确的顺序。
输入描述：
输入为一行，以空格分隔的喊”过“的次数，注意K并不提供（K不超过200），而数字的个数为N。
输出：
数组的第i个元素存储的是第i个人喊”过“的次数（即还原成正确的顺序）。
例子
输入
0 1 0
输出
1 0 0
只有一次过 发生在7 按顺序编号1的人遇到7; 注意：结束时的k不一定是7 也可以是 8 9
例子2
输入
0 0 0 2 1
输出
0 2 0 1 0
一共三次喊过
发生在7 14 17
编号为2 的遇到7 17
编号为4 的遇到14
"""
def is_pass(num):
    # 判断一个数字是否要喊“过”：数字是7的倍数或数字中包含7
    return num % 7 == 0 or '7' in str(num)

def restore_pass_order(over_count):
    n = len(over_count)     # 总人数
    total_passes = [0] * n  # 用于模拟每个人喊“过”的次数

    # 模拟喊数过程，直到喊够所有的喊“过”次数
    total_pass_count = sum(over_count)  # 需要喊“过”的总次数
    current_pass_count = 0  # 当前喊过的次数
    person_index = 0        # 从第1个人开始
    number = 1              # 从数字1开始喊

    while current_pass_count < total_pass_count:
        if is_pass(number):
            total_passes[person_index] += 1     # 记录某人喊到
            current_pass_count += 1
        person_index = (person_index + 1) % n   # 顺时针轮转，取模操作保证循环而不越界
        number += 1

    # 映射乱序的喊“过”次数回正确顺序
    result = [0] * n
    used = [False] * n  # 标记哪些乱序元素已使用
    for i in range(n):
        for j in range(n):
            if not used[j] and over_count[j] == total_passes[i]:
                result[i] = over_count[j]
                used[j] = True
                break

    return result

# 输入处理
over_counts_raw = "0 0 0 2 1"
over_counts_raw = "0 1 0"
over_counts = list(map(int, over_counts_raw.split()))

# 还原顺序
result = restore_pass_order(over_counts)

# 输出还原的顺序
print(" ".join(map(str, result)))

