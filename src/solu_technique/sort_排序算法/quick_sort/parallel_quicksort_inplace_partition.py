from concurrent.futures import ThreadPoolExecutor
from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1  # i是较小元素的索引
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr: List[int], low: int, high: int, executor, threshold=1000):
    if low < high:
        # 执行分区操作
        pi = partition(arr, low, high)

        # 如果分区大小大于阈值则并行处理
        if (high - low) > threshold:
            # 提交左右两部分的并行任务
            left_future = executor.submit(
                quicksort, arr, low, pi - 1, executor, threshold
            )
            right_future = executor.submit(
                quicksort, arr, pi + 1, high, executor, threshold
            )
            # 等待任务完成
            left_future.result()
            right_future.result()
        else:
            # 小于阈值时直接递归处理
            quicksort(arr, low, pi - 1, executor, threshold)
            quicksort(arr, pi + 1, high, executor, threshold)


def parallel_quicksort(arr: List[int]):
    # 使用ThreadPoolExecutor进行并行化
    with ThreadPoolExecutor() as executor:
        quicksort(arr, 0, len(arr) - 1, executor)


if __name__ == "__main__":
    # 测试
    arr = [10, 7, 8, 9, 1, 5]
    parallel_quicksort(arr)
    print("Sorted array is:", arr)
