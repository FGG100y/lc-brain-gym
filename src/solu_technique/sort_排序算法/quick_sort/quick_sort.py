"""
快速排序（quick sort）
1. 找到Pivot
2. 以pivot对数组进行分区，less 和 greater
3. 递归对分区进行快速排序
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    quick_sort_inplace(arr, 0, len(arr)-1)
    #  return quick_sort_inplace(arr, 0, len(arr)-1)    # return 的是 None ！


def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx-1)
        quick_sort_inplace(arr, pivot_idx+1, high)


def partition(arr, low, high):
    # 利用pivot对数组分区，返回pivot本身的索引
    pivot = arr[high]
    i = low - 1                                 # ??
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 把pivot放到正确的位置
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


def quick_sort2(arr):
    # 递归终止条件：如果数组长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr

    # 1. 选择基准（pivot），这里选择数组的最后一个元素
    pivot = arr[-1]

    # 2. 定义三个数组：分别存储小于、等于、大于基准的元素
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    # 3. 递归排序左右部分并拼接
    return quick_sort2(less) + [pivot] + quick_sort2(greater)



if __name__ == "__main__":
    arr = [1, 4, 4, 6, 2, 23, 45, 11]
    print(quick_sort2(arr))
    quick_sort(arr)                     # 原地排序，无返回值
    print(arr)
