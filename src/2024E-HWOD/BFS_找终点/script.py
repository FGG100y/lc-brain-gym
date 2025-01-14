"""
题⽬描述：
给定⼀个正整数数组，设为 nums ，最⼤为100个成员，求从第⼀个成员开始，正好⾛到数组 最后⼀
个成员，所使⽤的最少步骤数。
要求：
1、第⼀步必须从第⼀元素开始，且 1<=第⼀步的步⻓长 <= len(nums)/2 ；

2、从第⼆步开始，只能以所在成员的数字⾛相应的步数，不能多也不能少，如果⽬标不可达 返回-1；

3、只能向数组的尾部⾛，不能往回⾛。

输⼊描述：
由正整数组成的数组，以空格分隔，数组⻓长度⼩于100，请⾃⾏解析数据数量。

输出描述：
正整数，表示最少的步数；如果不存在输出-1。

示例1:
输⼊：7 5 9 4 2 6 8 3 5 4 3 9
输出：2

示例2:
输入：1 2 3 7 1 5 9 3 2 1
输出：-1
"""
from collections import deque

def min_steps(nums):
    n = len(nums)
    if n == 0:
        return -1

    # 初始化队列, 队列中的每个元素为 (当前下标, 当前步数)
    queue = deque()

    # 第一步的步长在 1 到 len(nums) // 2 之间
    for first_step in range(1, n // 2 + 1):
        if first_step < n:
            queue.append((first_step, 1))  # (索引, 步数)

    visited = set()  # 记录访问过的位置
    visited.add(0)  # 第一个元素默认访问过

    # BFS 开始
    while queue:
        index, steps = queue.popleft()

        # 到达数组末尾，返回步数
        if index >= n - 1:
            return steps

        # 获取当前可以跳的步长
        jump = nums[index]

        # 扩展新的可达位置
        next_index = index + jump
        if next_index < n and next_index not in visited:
            queue.append((next_index, steps + 1))
            visited.add(next_index)

    # 如果队列为空且没有找到解，返回-1
    return -1


nums_raw = "7 5 9 4 2 6 8 3 5 4 3 9"
nums_raw = "1 2 3 7 1 5 9 3 2 1"
nums = list(map(int, nums_raw.split()))
print(min_steps(nums))
