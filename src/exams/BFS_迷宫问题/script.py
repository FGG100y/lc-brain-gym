"""
描述
定义一个二维数组 N*M ，如 5 × 5 数组下所示：

int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编
程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。

数据范围：2≤n,m≤10  ， 输入的内容只包含0≤val≤1

输入描述：
输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以
走的路。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出描述：
左上角到右下角的最短路径，格式如样例所示。

示例1
输入：
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

输出：
(0,0)
(1,0)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
(3,4)
(4,4)

示例2
输入：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 1
0 1 1 1 0
0 0 0 0 0

输出：
(0,0)
(1,0)
(2,0)
(3,0)
(4,0)
(4,1)
(4,2)
(4,3)
(4,4)

说明：
注意：不能斜着走！！
"""

#  import sys
from collections import deque


def bfs_find_path(maze):    # bfs 通常采用迭代方式完成结点搜索
    rows, cols = len(maze), len(maze[0])

    if maze[0][0] == 1 or maze[rows - 1][cols - 1] == 1:
        return None

    # up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 当前位置坐标组和路径
    init_x, init_y = 0, 0
    init_path = [(0, 0)]                                    # 可变列表，方便后续添加路径
    queue = deque([((init_x, init_y), init_path)])          # list of tuples
    visited = set((init_x, init_y))                         # 访问过的坐标组

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == (rows - 1, cols - 1):                  # 到达终点
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy                         # 新坐标组
            if (
                0 <= nx < rows and 0 <= ny < cols           # 在边界内
                and maze[nx][ny] == 0                       # 是通道
                and (nx, ny) not in visited                 # 未访问过
            ):
                new_coor = (nx, ny)                         # 满足条件的新点
                visited.add(new_coor)
                queue.append((new_coor, path + [new_coor]))

    return None


#  ins = []
#  for line in sys.stdin:
#      a = line.strip().split()
#      ins.append(list(map(int, a)))
#
#  maze = ins[1:]

maze_raw = """
0 1 0 0 0
0 1 0 1 0
0 0 0 0 1
0 1 1 1 0
0 0 0 0 0
"""
maze_raw = """
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
0 1 1 1 0
1 0 0 0 0
"""
maze = [list(map(int, line.split())) for line in maze_raw.strip("\n").splitlines()]
#  print(maze)
#  print(len(maze), len(maze[0]))
#  breakpoint()

for pos in bfs_find_path(maze):
    res = ",".join([str(i) for i in pos])  # 否则报错格式不一致
    print(f"({res})")
