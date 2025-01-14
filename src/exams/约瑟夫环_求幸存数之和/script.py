def surviver_sum(nums, jump, left):
    # Josephus Promblem variant

    index = 0
    while len(nums) > left:
        index = (index + jump + 1) % len(nums)
        #  print(nums[index], end=" ")
        nums.pop(index)
        index -= 1  # 该数被敲出，并从该点起跳

    #  print(nums)
    return sum(nums)


left = 3
jump = 4
nums_raw = "[1,2,3,4,5,6,7,8,9]"
nums = list(map(int, nums_raw[1:-1].replace(",", "")))
ans = 13
assert surviver_sum(nums, jump, left) == ans
