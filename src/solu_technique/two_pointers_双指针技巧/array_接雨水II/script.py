"""
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形
状最多能接多少体积的雨水。
"""
import heapq

def trap_rain_water(heightMap):
    # 每个柱体的高度由三维坐标中的一个高度矩阵来表示。
    # 使用优先队列（堆）来实现类似二维问题的“外圈往内圈”的遍历策略，外层的首先放入堆中，
    # 并记录当前的最低边界。然后根据最低的边界高度与内层的高度比较，计算水量，并不断推进
    # 直到处理完所有的内层柱体。
    # 每次从（最小）堆取出当前高度最小的柱体，查看其邻居(与前后左右相比)，是否能够存储水，
    # 然后将邻居加入堆中，迭代检查。
    # 保证堆中始终存储的是外围边界。
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    total_water = 0
    heap = []

    # 初始化：将最外圈所有柱子放入堆中
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:    # 最外圈元素（想象俯瞰图）
                heapq.heappush(heap, (heightMap[i][j], i, j))   # 柱子的高，行，列
                visited[i][j] = True

    # 方向向量，用来处理四个邻居（上、下、左、右）
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        height, x, y = heapq.heappop(heap)  # 取出最小高度元素
        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                total_water += max(0, height - heightMap[nx][ny])
                heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                visited[nx][ny] = True
    return total_water


def trapRainWater(heightMap):               # Qwen2.5-coder-instruct
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    pq = []

    # 将边界加入优先队列
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    water_trapped = 0

    while pq:
        current_height, i, j = heapq.heappop(pq)

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                if heightMap[ni][nj] < current_height:
                    water_trapped += current_height - heightMap[ni][nj]
                    heightMap[ni][nj] = current_height

                heapq.heappush(pq, (heightMap[ni][nj], ni, nj))
                visited[ni][nj] = True

    return water_trapped


heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(trap_rain_water(heightMap))   # 4

heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
print(trap_rain_water(heightMap))   # 输出: 10
print(trapRainWater(heightMap))
