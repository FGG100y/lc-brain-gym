"""
parallel scan 算法（prefix sum）是高效处理数组前缀和的并行计算方法，目标是通过分治法和并
行计算来快速计算前缀和，而非顺序地逐项累加。

prefix sum的目的是，对于一个输入数组 a1,a2,...,an ，生成一个输出数组 s1,s2,...,sn，使得
每个 si 等于 a1+a2+...+ai 的和。

在顺序扫描中，计算每个前缀和的时间复杂度为 O(n)。而通过parallel scan算法，借助并行计算，
时间复杂度可以降低为 O(logn)。

算法过程

假设我们有一个长度为 8 的数组：[a, b, c, d, e, f, g, h]，过程如下：

上升阶段（Reduce）：
    第 1 层：相邻两数相加形成 4 个新值：[a+b, c+d, e+f, g+h]
    第 2 层：将上一层的相邻值相加形成 2 个新值：[(a+b)+(c+d), (e+f)+(g+h)]
    第 3 层：继续相加得到最终总和：[(a+b+c+d)+(e+f+g+h)]

下降阶段（Down-sweep）：
    自顶向下分配前缀和，依次更新每个位置的值，直到生成完整的前缀和数组。
"""

#  from multiprocessing import Pool, cpu_count
import numpy as np


def up_sweep(arr):
    n = len(arr)
    step = 1
    while step < n:
        for i in range(0, n, step * 2):
            if i + step < n:
                arr[i + step*2 - 1] += arr[i + step - 1]
        step *= 2
    return arr


def down_sweep(arr):
    n = len(arr)
    step = n // 2
    arr[-1] = 0
    while step > 0:
        for i in range(0, n, step * 2):
            if i + step < n:
                temp = arr[i + step - 1]
                arr[i + step - 1] = arr[i + step * 2 - 1]
                arr[i + step * 2 - 1] += temp
        step //= 2
    return arr


def parallel_scan(arr):
    n = len(arr)

    padded_size = 1 << (n-1).bit_length()
    if padded_size > n:
        arr = np.concatenate((arr, [0] * (padded_size - n)))

    last_element = arr[n-1]

    arr = up_sweep(arr)
    arr = down_sweep(arr)

    arr[n-1]  += last_element

    return arr[:n]


if __name__ == "__main__":
    arr = np.array([3, 1, 7, 0, 4, 1, 6, 3])
    result = parallel_scan(arr)
    print("Original array:", arr)
    print("Prefix sum (parallel scan):", result)    # [ 0  3  4 11 11 15 16 22 25]
