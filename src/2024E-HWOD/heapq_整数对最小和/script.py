"""
题目描述
给定两个整数数组array1、array2，数组元素按升序排列。
假设从array1、array2中分别取出一个元素可构成一对元素，现在需要取出k对元素，
并对取出的所有元素求和，计算和的最小值。
注意：
两对元素如果对应于array1、array2中的两个下标均相同，则视为同一对元素。
输入描述
输入两行数组array1、array2，每行首个数字为数组大小size(0 < size <= 100);
0 < array1[i] <= 1000
0 < array2[i] <= 1000
接下来一行为正整数k
0 < k <= array1.size() * array2.size()
输出描述
满足要求的最小和
用例
输入
3 1 1 2
3 1 2 3
2
输出
4
说明
用例中，需要取2对元素
取第一个数组第0个元素与第二个数组第0个元素组成1对元素[1,1];
取第一个数组第1个元素与第二个数组第0个元素组成1对元素[1,1];
求和为1+1+1+1=4，为满足要求的最小和。
"""
import heapq

def find_k_pairs_min_sum(array1, array2, k):
    size1, size2 = len(array1), len(array2)

    # 小顶堆初始化：将 array1[0] 和 array2 中的每个元素组合，加入堆
    min_heap = []
    for j in range(size2):
        heapq.heappush(min_heap, (array1[0] + array2[j], 0, j))

    result_sum = 0

    # 弹出 k 个最小和组合
    for _ in range(k):
        curr_sum, i, j = heapq.heappop(min_heap)
        result_sum += curr_sum

        # 如果 array1 还有下一个元素，把 array1[i+1] 和 array2[j] 的组合加入堆
        if i + 1 < size1:
            heapq.heappush(min_heap, (array1[i+1] + array2[j], i + 1, j))

    return result_sum

#  # 输入处理
#  def process_input():
#      array1 = list(map(int, input().split()))[1:]  # 去掉首个数组大小
#      array2 = list(map(int, input().split()))[1:]  # 去掉首个数组大小
#      k = int(input().strip())  # 读取k值
#      return array1, array2, k
#
#  # 调用输入处理函数
#  array1, array2, k = process_input()

array1 = list(map(int, "3 1 1 2".split()[1:]))
array2 = list(map(int, "3 1 2 3".split()[1:]))
k = 3
# 计算并输出最小和
result = find_k_pairs_min_sum(array1, array2, k)
print(result)

