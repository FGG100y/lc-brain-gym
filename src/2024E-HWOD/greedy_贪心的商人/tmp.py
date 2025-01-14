def max_profit(number, days, item, item_price):
    total_profit = 0

    # 遍历每种商品
    for i in range(number):
        max_quantity = item[i]  # 当前商品的最大持有量

        # 计算每种商品的最大利润
        for day in range(1, days):
            # 如果今天的价格比昨天高，则可以获取利润
            if item_price[i][day] > item_price[i][day - 1]:
                # 价格差值 * 最大持有量
                profit = (item_price[i][day] - item_price[i][day - 1]) * max_quantity
                total_profit += profit

    return total_profit

# 输入处理
number = 3
days = 3
item = [4, 5, 6]
item_price_raw = """
1 2 3
4 3 2
1 5 2
"""
item_price = [list(map(int, row.split())) for row in item_price_raw.strip("\n").split("\n")]

# 输出最大利润
print(max_profit(number, days, item, item_price))

