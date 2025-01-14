def max_investment(products, total_investment, max_risk, returns, risks, limits):
    # 记录最佳投资方式
    best_investment = [0] * products
    max_return = 0

    # 枚举两个产品的组合
    for i in range(products):
        for j in range(i+1, products):
            # 投资i和j产品的最大可能组合
            for invest_i in range(0, min(limits[i], total_investment) + 1):
                invest_j = min(limits[j], total_investment - invest_i)

                if invest_j <= limits[j]:
                    # 计算当前组合的总风险和总回报
                    total_risk = risks[i]+ risks[j]
                    total_return = returns[i] * invest_i + returns[j] * invest_j

                    # 如果总风险在可接受范围内，且回报更优，更新最佳方案
                    if total_risk <= max_risk and total_return > max_return:
                        max_return = total_return
                        best_investment = [0] * products
                        best_investment[i] = invest_i
                        best_investment[j] = invest_j


    return best_investment

# 测试用例
products = 5
total_investment = 100
max_risk = 10
returns = [10, 20, 30, 40, 50]
risks = [3, 4, 5, 6, 10]
limits = [20, 30, 20, 40, 30]

# 输出最佳投资方案
print(max_investment(products, total_investment, max_risk, returns, risks, limits))
