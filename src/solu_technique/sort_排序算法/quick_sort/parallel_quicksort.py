#  import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    # 分区操作
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # 定义两个进程池，用于并行排序左右子数组
    #  with multiprocessing.Pool(processes=2) as pool:
    #  with multiprocessing.get_context("spawn").Pool(processes=2) as pool:
    #      sorted_left, sorted_right = pool.map(quick_sort, [left, right])
    #  AssertionError: daemonic processes are not allowed to have children

    with ProcessPoolExecutor(max_workers=2) as executor:
        sorted_left, sorted_right = executor.map(quick_sort, [left, right])

    return sorted_left + [pivot] + sorted_right


if __name__ == "__main__":
    arr = [9, 4, 8, 3, 1, 2, 5, 7, 6]
    sorted_arr = quick_sort(arr)
    print("Sorted Array:", sorted_arr)
