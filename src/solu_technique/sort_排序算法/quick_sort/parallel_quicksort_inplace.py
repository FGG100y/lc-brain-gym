import multiprocessing


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def parallel_inplace(arr, low, high, max_depth=2):
    if low < high:
        # 原地分区
        pivot_index = partition(arr, low, high)

        # 控制递归深度以防止过多进程
        if max_depth > 0:
            # 并行执行左右子数组的排序
            left_process = multiprocessing.Process(
                target=parallel_inplace,
                args=(arr, low, pivot_index - 1, max_depth - 1),
            )
            right_process = multiprocessing.Process(
                target=parallel_inplace,
                args=(arr, pivot_index + 1, high, max_depth - 1),
            )
            left_process.start()
            right_process.start()
            left_process.join()
            right_process.join()
        else:
            # 达到最大递归深度时，转为单线程处理
            parallel_inplace(arr, low, pivot_index - 1, 0)
            parallel_inplace(arr, pivot_index + 1, high, 0)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    parallel_inplace(arr, 0, len(arr)-1)

if __name__ == "__main__":
    arr = [9, 4, 8, 3, 1, 2, 5, 7, 6]
    quick_sort(arr)
    print("Sorted Array:", arr)
