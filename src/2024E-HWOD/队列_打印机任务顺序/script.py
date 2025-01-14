"""
题目描述
某个打印机根据打印队列执行打印任务。打印任务分为九个优先级，分别用数字1-9表示，数字越大
优先级越高。打印机每次从队列头部取出第一个任务A，然后检查队列余下任务中有没有比A优先级更
高的任务，如果有比A优先级高的任务，则将任务A放到队列尾部，否则就执行任务A。
请编写一个程序，根据输入的打印队列，输出实际的打印顺序。
输入描述
输入一行，为每个任务的优先级，优先级之间用逗号隔开，优先级取值范围是1~9。
输出描述
输出一行，为每个任务的打印顺序，打印顺序从0开始，用逗号隔开
示例1
输入
9,3,5
输出
0,2,1
说明·队列头部任务的优先级为9，最先打印，故序号为0；接着队列头部任务优先级为3，队列中还有
优先级为5的任务，优先级3任务被移到队列尾部；接着打印优先级为5的任务，故其序号为1；最后优
先级为3的任务的序号为2。
"""
from collections import deque

def print_order(input_string):
    """
    根据打印队列的优先级计算实际的打印顺序
    """
    # 将输入的优先级转化为队列，并标记每个任务的原始索引
    tasks = deque((i, int(p)) for i, p in enumerate(input_string.split(',')))

    result = []  # 用来存储打印顺序

    # 模拟打印任务的处理
    while tasks:
        current = tasks.popleft()  # 取出队列头部任务
        # 检查是否存在优先级更高的任务
        if any(current[1] < other[1] for other in tasks):
            tasks.append(current)  # 如果有更高优先级的任务，移到队列尾部
        else:
            result.append(current[0])  # 否则执行任务，记录其原始索引

    return ','.join(map(str, result))


def prt_order(arr):
    # 构建字典{idx:val},考虑有重复的同等级任务
    # 遍历arr数组，每个val可能对应多个idx，排序后就是它们的顺序
    # 因为同级的元素在arr数组中散布，故借助一个状态表来记录其顺序
    # 最终返回状态表
    result = [0] * len(arr)
    idx2val_map = {idx:val for idx, val in enumerate(sorted(arr, reverse=True))}

    for v in set(arr):
        ori_indices = [i for i, n in enumerate(arr) if v == n]
        res_indices = [i for i, n in idx2val_map.items() if v == n]
        for oi, ri in zip(ori_indices, res_indices):
            result[oi] = ri
    return result


arr = [9,9,3,5,9]
out = [0,1,4,3,2]
print(prt_order(arr))
assert prt_order(arr) == out

arr = "9,9,3,5,9"
out = "0,1,4,3,2"
print(print_order(arr))
assert print_order(arr) == out
