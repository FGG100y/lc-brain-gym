"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

想象二维平面中的柱状图，高柱子和矮柱子之间可以“接雨水”。
"""
def trap(heights):
    # 双指针:维护左右两个最大值来计算能接住的雨水量
    # 从左到右：如果当前柱子比左边最大值小，则可以接水，接水量=left_max - current
    # 从右到左：如果当前柱子比右边最大值小，则可以接水，接水量=right_max - current
    # 最终接水量：比较左右两个最大值，以较小那一个为准计算接水量

    if not heights:
        return 0

    left, right = 0, len(heights)-1
    left_max, right_max = heights[left], heights[right]
    total_water = 0

    while left < right: # 双指针向中间靠拢
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            total_water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            total_water += right_max - heights[right]

    return total_water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
assert trap(height) == 6

height = [4,2,0,3,2,5]
print(trap(height))
assert trap(height) == 9
