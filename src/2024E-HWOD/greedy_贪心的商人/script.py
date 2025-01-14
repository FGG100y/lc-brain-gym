def find_max_profit(item_price, max_items):
    # 获利原则：低价进，高价出
    # 对每一种商品，选最低价那天进货，选最高价那天出货；进货数量受限于仓库限制
    # 只要items[i]进货价格低于出货价格，则这个商品就能在days天内获利
    # 贪心算法：计算每一种组合，选择获利最高那一种
    total_profit = 0
    num_items = len(item_price)
    num_days = len(item_price[0])

    for i in range(num_items):
        max_quanto = max_items[i]

        for day in range(1, num_days):
            # 如果今天价格比昨天高，就有利润
            if item_price[i][day] > item_price[i][day - 1]:
                # 可卖出的最大数量 * 价差
                profit = max_quanto * (item_price[i][day] - item_price[i][day - 1])
                total_profit += profit
    #  print(total_profit)
    return total_profit


items = 3
days = 3
max_items = [4, 5, 6]
item_price_raw = """
1 2 3
4 3 2
1 5 2
"""
item_price = [list(map(int, row.split())) for row in item_price_raw.strip("\n").split("\n")]
assert find_max_profit(item_price, max_items) == 32
