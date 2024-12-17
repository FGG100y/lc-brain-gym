import numpy as np
from multiprocessing import Pool

# 上升阶段：计算部分和
def upsweep(arr):
    n = len(arr)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            if i + step < n:
                arr[i + 2 * step - 1] += arr[i + step - 1]
        step *= 2
    return arr

# 下降阶段：更新前缀和
def downsweep(arr):
    n = len(arr)
    arr[-1] = 0  # 最后一个元素置零
    step = n // 2
    while step > 0:
        for i in range(0, n, 2 * step):
            if i + step < n:
                t = arr[i + step - 1]
                arr[i + step - 1] = arr[i + 2 * step - 1]
                arr[i + 2 * step - 1] += t
        step //= 2
    return arr

# 并行前缀和
def parallel_scan(arr):
    arr = upsweep(arr.copy())
    arr = downsweep(arr)
    return arr

# 示例
arr = np.array([3, 1, 7, 0, 4, 1, 6, 3])
prefix_sum = parallel_scan(arr)
print("并行前缀和结果:", prefix_sum)  # [ 0  3  4 11 11 15 16 22]

