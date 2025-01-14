def dfs_find_cipher_path(n, data, m, matrix):   # dfs 通常采用递归方式完成结点搜索
    # 定义方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 存储所有合法路径
    all_paths = []

    def dfs(x, y, index, path, visited):
        # 如果当前找到的数字和明文匹配
        if matrix[x][y] == data[index]:
            # 记录当前位置
            path.append((x, y))
            # 如果已经匹配到最后一个字符，存储路径
            if index == n - 1:
                all_paths.append(path[:])
            else:
                # 深度优先搜索相邻的四个方向
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    # 判断新位置是否越界和是否已经访问过
                    if 0 <= new_x < m and 0 <= new_y < m and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        dfs(new_x, new_y, index + 1, path, visited)
                        visited.remove((new_x, new_y))
            path.pop()

    # 遍历密码本的所有位置，寻找明文的起点
    for i in range(m):
        for j in range(m):
            if matrix[i][j] == data[0]:  # 找到与明文第一位匹配的起点
                visited = set()
                visited.add((i, j))
                dfs(i, j, 0, [], visited)

    # 如果找不到任何路径，返回error
    if not all_paths:
        return "error"

    # 将所有找到的路径转换为密文格式
    encoded_paths = []
    for path in all_paths:
        encoded = []
        for x, y in path:
            encoded.append(f"{x} {y}")
        encoded_paths.append(" ".join(encoded))

    # 返回字典序最小的密文
    return min(encoded_paths)

# 输入处理
n = int(input().strip())
data = list(map(int, input().strip().split()))
m = int(input().strip())
matrix = [list(map(int, input().strip().split())) for _ in range(m)]

# 输出结果
print(dfs_find_cipher_path(n, data, m, matrix))

