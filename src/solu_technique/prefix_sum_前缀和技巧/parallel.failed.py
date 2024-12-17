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

#  from multiprocessing import Array, Pool, cpu_count
#
#  import numpy as np
#
#
#  def up_sweep_step(arr, step, n):
#      """每个进程在给定的步长下进行上升阶段的加法操作。"""
#      for i in range(step - 1, n - 1, step * 2):
#          arr[i + step] += arr[i]
#
#
#  def down_sweep_step(arr, step, n):
#      """每个进程在给定的步长下进行下降阶段的加法操作。"""
#      for i in range(step - 1, n - 1, step * 2):
#          temp = arr[i]
#          arr[i] = arr[i + step]
#          arr[i + step] += temp
#
#
#  def parallel_scan(arr):
#      n = len(arr)
#      padded_size = 1 << (n - 1).bit_length()  # 将大小扩展到最近的2的幂次
#
#      # 使用共享内存数组，以便子进程可以访问
#      shared_arr = Array("i", list(arr) + [0] * (padded_size - n))
#
#      # 获取进程数
#      num_workers = cpu_count()
#
#      # 上升阶段
#      step = 1
#      while step < padded_size:
#          with Pool(num_workers) as pool:
#              # 使用多个进程在共享数组上执行上升阶段加法
#              pool.starmap(up_sweep_step, [(shared_arr, step, padded_size)] * num_workers)
#          step *= 2
#
#      # 设置最后一个元素为0
#      shared_arr[padded_size - 1] = 0
#
#      # 下降阶段
#      step = padded_size // 2
#      while step > 0:
#          with Pool(num_workers) as pool:
#              # 使用多个进程在共享数组上执行下降阶段加法
#              pool.starmap(
#                  down_sweep_step, [(shared_arr, step, padded_size)] * num_workers
#              )
#          step //= 2
#
#      # 将共享数组转换回普通数组并去除填充
#      result = list(shared_arr)[:n]
#      return result


#  from multiprocessing import Pool, Array, cpu_count
#  import numpy as np
#
#  # 定义一个全局共享数组
#  shared_arr = None
#
#  def init_shared_array(arr):
#      """初始化共享数组，使子进程可以访问共享内存"""
#      global shared_arr
#      shared_arr = arr
#
#  def up_sweep_step(step, n):
#      """每个进程在给定的步长下进行上升阶段的加法操作。"""
#      global shared_arr
#      for i in range(step - 1, n - 1, step * 2):
#          shared_arr[i + step] += shared_arr[i]
#
#  def down_sweep_step(step, n):
#      """每个进程在给定的步长下进行下降阶段的加法操作。"""
#      global shared_arr
#      for i in range(step - 1, n - 1, step * 2):
#          temp = shared_arr[i]
#          shared_arr[i] = shared_arr[i + step]
#          shared_arr[i + step] += temp
#
#  def parallel_scan(arr):
#      n = len(arr)
#      padded_size = 1 << (n - 1).bit_length()  # 将大小扩展到最近的2的幂次
#
#      # 使用共享内存数组，以便子进程可以访问
#      shared_array = Array('i', list(arr) + [0] * (padded_size - n))
#
#      # 获取进程数
#      num_workers = cpu_count()
#
#      # 初始化池并注册共享数组
#      with Pool(num_workers, initializer=init_shared_array, initargs=(shared_array,)) as pool:
#          # 上升阶段
#          step = 1
#          while step < padded_size:
#              # 使用多个进程在共享数组上执行上升阶段加法
#              pool.starmap(up_sweep_step, [(step, padded_size)] * num_workers)
#              step *= 2
#
#          # 设置最后一个元素为0
#          shared_array[padded_size - 1] = 0
#
#          # 下降阶段
#          step = padded_size // 2
#          while step > 0:
#              # 使用多个进程在共享数组上执行下降阶段加法
#              pool.starmap(down_sweep_step, [(step, padded_size)] * num_workers)
#              step //= 2
#
#      # 将共享数组转换回普通数组并去除填充
#      result = list(shared_array)[:n]
#      return result


import numpy as np
from concurrent.futures import ThreadPoolExecutor

def parallel_scan(arr):
    n = len(arr)
    if n == 0:
        return arr

    # 向上推进（Up-Sweep）阶段
    def up_sweep(d, offset):
        for i in range(0, n, 2 ** (d + 1)):
            arr[i + 2 ** (d + 1) - 1] += arr[i + 2 ** d - 1]

    # 向下推进（Down-Sweep）阶段
    def down_sweep(d, offset):
        for i in range(0, n, 2 ** (d + 1)):
            temp = arr[i + 2 ** d - 1]
            arr[i + 2 ** d - 1] = arr[i + 2 ** (d + 1) - 1]
            arr[i + 2 ** (d + 1) - 1] += temp

    # Up-Sweep操作
    with ThreadPoolExecutor() as executor:
        for d in range(int(np.log2(n))):
            futures = [executor.submit(up_sweep, d, offset) for offset in range(2 ** (d + 1))]
            [f.result() for f in futures]

    # 设置根节点为0
    arr[-1] = 0

    # Down-Sweep操作
    with ThreadPoolExecutor() as executor:
        for d in range(int(np.log2(n)) - 1, -1, -1):
            futures = [executor.submit(down_sweep, d, offset) for offset in range(2 ** (d + 1))]
            [f.result() for f in futures]

    return arr


if __name__ == "__main__":
    arr = np.array([3, 1, 7, 0, 4, 1, 6, 3])
    result = parallel_scan(arr)
    print("Original array:", arr)
    print("Prefix sum (parallel scan):", result)
