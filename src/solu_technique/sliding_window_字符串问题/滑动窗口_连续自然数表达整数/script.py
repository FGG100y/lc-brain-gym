def find_continuous_sums(target, verbose=True):
    # 初始化计数器和结果列表
    count = 0
    results = []

    # 初始化窗口的开始位置和当前窗口内的总和
    start = 1
    current_sum = 0

    # 遍历可能的结束位置
    for end in range(1, target + 1):
        # 添加当前结束位置的数到窗口内
        current_sum += end

        # 当当前窗口内的总和大于目标值时，减去窗口开始位置的数并移动开始位置
        while current_sum > target:
            current_sum -= start
            start += 1

        # 当当前窗口内的总和等于目标值时，记录结果并移动开始位置
        if current_sum == target:
            sequence = '+'.join(map(str, range(start, end + 1)))
            results.append(f"{target}={sequence}")
            count += 1

            current_sum -= start
            start += 1

    if verbose:
        # 输出结果
        for seq in results[::-1]:
            print(seq)
        print(f"Result:{count}")

    return results

# 示例输入
target = 10
target = 12
find_continuous_sums(target)
