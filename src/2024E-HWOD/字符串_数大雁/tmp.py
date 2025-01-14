def count_geese(cry: str) -> int:
    stages = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}
    stage_count = [0] * 5  # 用来跟踪每个阶段的字符数，按quack顺序
    max_geese = 0  # 记录大雁的最大数量
    active_geese = 0  # 当前同时发声的活跃大雁数

    for char in cry:
        if char not in stages:
            return -1  # 非法字符

        stage_index = stages[char]  # 获取当前字符的阶段

        if stage_index == 0:
            # 一个新的 'q'，意味着要启动一只新的大雁
            stage_count[0] += 1
            active_geese += 1
            max_geese = max(max_geese, active_geese)
        else:
            # 检查之前阶段是否满足
            if stage_count[stage_index - 1] > 0:
                stage_count[stage_index - 1] -= 1
                stage_count[stage_index] += 1
                if char == 'k':
                    # 一只大雁完成了一个完整的 "quack"
                    active_geese -= 1
            else:
                # 如果前一阶段没有未处理的字符，说明顺序错了
                return -1

    # 检查所有的 'q', 'u', 'a', 'c' 是否都匹配完成了
    if any(stage_count[:-1]):
        return -1

    return max_geese

# 测试用例
print(count_geese("quackquack"))  # 输出: 1
print(count_geese("qaauucqcaa"))  # 输出: -1
print(count_geese("quacqkuackquack"))  # 输出: 2
print(count_geese("qququaauqccauqkkcauqqkcauuqkcaaukccakkck"))  # 输出: 5
print(count_geese("quacqkuquacqkacuqkackuack"))  # 输出: 3

