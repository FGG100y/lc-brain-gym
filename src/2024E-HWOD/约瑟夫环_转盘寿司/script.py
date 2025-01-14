

def sushi_prices(prices):
    n = len(prices)
    result = [0] * n  # 用于存储最终结果

    # 从左到右遍历每一盘寿司
    for i in range(n):
        result[i] = prices[i]  # 默认情况下，客户只获得当前盘子的价格

        # 从i+1开始，环状查找第一个比当前盘子价格低的寿司
        for j in range(1, n):
            next_index = (i + j) % n  # 通过取模运算实现环状
            if prices[next_index] < prices[i]:
                result[i] += prices[next_index]  # 找到后加上这个盘子的价格
                break

    #  print(result)
    return result

# 示例输入
prices = [3, 15, 6, 14, 4]
result = sushi_prices(prices)
assert " ".join(map(str, result)) == "3 21 10 18 7"
