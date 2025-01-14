from collections import defaultdict


def find_boss_and_calculate_income(relationships):
    # 初始化分销商收入表和分销商下级的字典
    income_map = {}
    subordinates = defaultdict(list)
    all_distributors = set()  # 所有分销商集合
    has_superior = set()       # 有上级的分销商集合

    # 构建分销商关系树
    for dist_id, parent_id, income in relationships:
        income_map[dist_id] = income
        all_distributors.add(dist_id)
        if parent_id != -1:  # 如果有上级分销商（-1 表示没有上级）
            subordinates[parent_id].append(dist_id)
            has_superior.add(dist_id)

    # 出现在 parent_id 但不在 dist_id 的就是 boss
    # 找到没有上级的分销商，就是boss
    boss_candidates = set(subordinates.keys()) - all_distributors 

    if len(boss_candidates) != 1:
        raise ValueError(f"输入数据不合法，{boss_candidates=}。")
    boss = boss_candidates.pop()

    # 递归计算总收入
    def compute_total_income(distributor):
        total_income = income_map.get(distributor, 0)
        # 计算下级分销商贡献的收入
        for sub in subordinates[distributor]:
            sub_income = compute_total_income(sub)
            total_income += sub_income // 100 * 15
        return total_income

    # 计算上交金额
    def compute_boss_income(distributor):
        #  total_income = 0  # boss只抽成
        total_income = income_map.get(distributor, 0)
        # 计算下级上交的金额
        for sub in subordinates[distributor]:
            sub_income = compute_total_income(sub)
            total_income += sub_income
        return total_income // 100 * 15

    # 计算boss收入
    boss_income = compute_boss_income(boss)

    return boss, boss_income

#  # 输入处理
#  N = int(input().strip())
#  relationships = []
#  for _ in range(N):
#      dist_id, parent_id, income = map(int, input().strip().split())
#      relationships.append((dist_id, parent_id, income))

#  N = 5
lines = """
1 0 100
2 0 200
3 0 300
4 0 200
5 0 200
"""
lines = """
1 0 223
2 1 323
3 2 1203
"""
relationships = []
for line in lines.strip("\n").split("\n"):
    dist_id, parent_id, income = map(int, line.split())
    relationships.append((dist_id, parent_id, income))
#  print(relationships)
#  breakpoint()

# 计算并输出boss收入
boss, boss_income = find_boss_and_calculate_income(relationships)
print(boss, boss_income)
