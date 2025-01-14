def count_geese(quack_str):
    # 每个完整的 quack 都对应潜在一只大雁，
    # 但只有交错出现的 quacqkuack 才代表同时活动的大雁，
    # 也就是每次碰上 k 都要减少一只同时活动的大雁 (active_geese)
    #
    # 需要一个 stage 记录各个阶段（字母）出现的情况，
    # u -> q
    # a -> u
    # c -> a
    # k -> c
    # 也就是如果叫声字符串是完整的，则每个后续的字母都有匹配的前一个字符，否则顺序错误


    #  stage_idx = {"q": 0, "u": 1, "a": 2, "c": 3, "k": 4, }
    stage_idx = {char:idx for idx, char in enumerate("quack")}
    stages = [0] * 5  # "q u a c k" 各个字母计数状态器
    active_geese = 0
    max_geese = 0

    for char in quack_str:
        if char not in stage_idx:
            return -1

        idx = stage_idx[char]
        if idx == 0:
            # 每个 q 都意味着一只大雁
            stages[idx] += 1
            active_geese += 1
            max_geese = max(active_geese, max_geese)
        else:
            if stages[idx-1] > 0:
                stages[idx-1] -= 1
                stages[idx] += 1
                if char == "k":
                    # 每个 k 意味着叫声结束
                    active_geese -= 1
            else:  # 前一个阶段已经处理完，而后一个阶段还没完，意味着序列顺序错误
                return -1

    if any(stages[:-1]):  # q u a c 应该都归零，否则序列错误
        return -1

    return max_geese

# 测试用例
print(count_geese("quackquack"))  # 输出: 1
print(count_geese("qaauucqcaa"))  # 输出: -1
print(count_geese("quacqkuackquack"))  # 输出: 2
print(count_geese("qququaauqccauqkkcauqqkcauuqkcaaukccakkck"))  # 输出: 5
print(count_geese("quacqkuquacqkacuqkackuack"))  # 输出: 3
