def find_plant_area(matrix, region_len, region_wid, size, min_power):
    # 矩阵中找连续区域，滑动窗口技巧
    result = []
    for i in range(region_len - size + 1):  # size: 正方形边长
        for j in range(region_wid - size + 1):
            total_power = 0  # 所选区域总发电量（要大于min_power）
            for x in range(size):
                for y in range(size):
                    total_power += matrix[i+x][j+y]
                    # 但如果所选区域中有0，则不适合建厂，跳过
                    if matrix[i+x][j+y] == 0:
                        total_power = 0
            if total_power > min_power:
                result.append(((i, j), total_power))
    return result  # result 为空，则没找到合适区域

metadata = "3 5 2 6"
region_len, region_wid, size, min_power = list(map(int, metadata.split()))
matrix_raw = """
1 3 4 5 8
0 4 5 0 0
2 3 6 7 1
"""
matrix = [list(map(int, row.strip().split())) for row in matrix_raw.strip("\n").split("\n")]
print(find_plant_area(matrix, region_len, region_wid, size, min_power))
