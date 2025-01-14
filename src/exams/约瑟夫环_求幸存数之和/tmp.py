def survive_sum(nums, jump, left):
    if left >= len(nums):
        return sum(nums)

    # 使用列表表示数字列
    nums_list = nums[:]
    current_index = 0

    while len(nums_list) > left:
        # 计算要删除的索引
        delete_index = (current_index + jump) % len(nums_list)
        # 删除对应的数字
        nums_list.pop(delete_index)
        # 更新当前起跳点
        current_index = delete_index % len(nums_list)

    print(nums_list)
    return sum(nums_list)

# 示例
print(survive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 3))  # 输出: 13

# GPT4o-mini, not so good.
