def optimal_investment(m, N, X, returns, risks, max_investments):
    best_investment = [0] * m
    max_return = 0

    # 遍历所有两两组合
    for i in range(m):
        for j in range(i+1, m):
            for invest_i in range(min(max_investments[i], N)+1):  # 投资额度限制
                invest_j = min(max_investments[j], N - invest_i)  # 只能投资两个产品
                total_risk = risks[i] + risks[j]
                if total_risk <= X:
                    total_return = invest_i * returns[i] + invest_j * returns[j]
                    if total_return > max_return:
                        max_return = total_return
                        best_investment = [0] * m  # 重置结果，以便更新最优组合
                        best_investment[i] = invest_i
                        best_investment[j] = invest_j
    return best_investment


# 输入
m, N, X = 5, 100, 10
returns = [10, 20, 30, 40, 50]
risks = [3, 4, 5, 6, 10]
max_investments = [20, 30, 20, 40, 30]

# 输出
result = optimal_investment(m, N, X, returns, risks, max_investments)
print(result)  # 输出: [0, 30, 0, 40, 0]
