

def max_gems_to_buy(gems, value):
    """Sliding Window"""
    # left index, right index, keep the window (of value constrain)
    max_gems = 0
    left = 0
    current_sum = 0

    for right in range(len(gems)):
        current_sum += gems[right]

        # when to move left: current_sum exceed value
        #  if current_sum > value:  # > BUGGY:左边小价格多的时候需要多次剔除
        while current_sum > value:
            current_sum -= gems[left]
            left += 1

        max_gems = max(max_gems, right - left + 1)

    return max_gems


value = 10
value = 15
gl = "8 4 6 3 1 6 7"
gl = "6 1 3 1 8 9 3 2 4"
gems = list(map(int, gl.split()))
print(max_gems_to_buy(gems, value))


def most_valued_individual_to_buy(gems, value):
    """Sliding Window"""
    # left index, right index, keep the window (of value constrain)
    max_avg_price = 0
    max_gems = 0
    left = 0
    current_sum = 0

    for right in range(len(gems)):
        current_sum += gems[right]

        while current_sum > value:
            current_sum -= gems[left]
            left += 1

        window_size = right - left + 1
        if window_size > 0:
            cur_avg_price = current_sum / window_size
            if cur_avg_price > max_avg_price:
                max_avg_price = cur_avg_price
                max_gems = window_size
    return max_gems


print(most_valued_individual_to_buy(gems, value))
