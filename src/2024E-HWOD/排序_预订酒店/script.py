def find_near_neighbors(arr, k, x):
    result = sorted(arr, key=lambda p: (abs(p - x), p))  # 按差值和数值本身进行排序
    return sorted(result[:k])

arr = [3, 4, 3, 7, 9, 6, 10, 4, 5, 6]
k = 3
x = 5
assert find_near_neighbors(arr, k, x) == [4, 4, 5]
