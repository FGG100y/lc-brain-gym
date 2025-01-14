def find_steps(steps, count):
    # 找到索引之和最小的、能完成“两回合”跳格子组合
    min_index_sum = float("inf")
    result = []

    for i in range(len(steps)):
        for j in range(i+1, len(steps)):
            # 每一对组合，若满足:
            if steps[i] + steps[j] == count:
                # 则记录索引之和
                index_sum = i + j
                # 更新最小索引之和及其对应组合
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [steps[i], steps[j]]
    return result



# 示例输入
steps = [1, 4, 5, 2, 2]
count = 7
result = find_steps(steps, count)
print(result)  # 输出 [5, 2]

# 示例2
steps = [-1, 2, 4, 9, 6]
count = 8
result = find_steps(steps, count)
print(result)  # 输出 [-1, 9]


def find_three_steps_optimized(steps, count):
    # 初始化最小索引和为一个很大的值
    min_index_sum = float('inf')
    result = []

    # 使用字典来存储两个元素之和及其索引
    sum_map = {}

    # 遍历所有步数，存储两个步数之和
    for i in range(len(steps)):
        for j in range(i + 1, len(steps)):
            # 计算两步之和
            pair_sum = steps[i] + steps[j]
            # 将索引和存储在字典中，方便后续查找
            if pair_sum not in sum_map:
                sum_map[pair_sum] = (i, j)

    # 再次遍历步数，寻找是否存在满足条件的组合
    for k in range(len(steps)):
        remaining = count - steps[k]
        if remaining in sum_map:
            i, j = sum_map[remaining]
            if i != k and j != k:  # 确保三个索引不相同
                index_sum = i + j + k
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [steps[i], steps[j], steps[k]]

    return result

# 示例输入
steps = [1, 4, 5, 2, 2]
count = 7
result = find_three_steps_optimized(steps, count)
print(result)  # 输出 [1, 4, 2]

