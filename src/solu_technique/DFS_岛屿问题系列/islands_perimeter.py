"""463. 岛屿的周长
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0
表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有
一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。
网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 1：
输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边

示例 2：
输入：grid = [[1]]
输出：4

示例 3：
输入：grid = [[1,0]]
输出：4
"""

def islands_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    def dfs(x, y):
        # 与边界相接，加一
        if not (0 <= x < rows and 0 <= y < cols):
            return 1
        # 从岛格走向水域，加一
        if grid[x][y] == 0:
            return 1
        # 从岛格走向岛格，加零
        if grid[x][y] != 1:
            return 0

        grid[x][y] = -1
        return dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += dfs(i, j)

    return perimeter


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islands_perimeter(grid))
#  输出：16
