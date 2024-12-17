"""leetcode 304. 二维区域和检索 - 矩阵不可变
给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角
(row2, col2) 所描述的子矩阵的元素 总和 。


示例 1：
[num-matrix](https://pic.leetcode-cn.com/1626332422-wUpUHT-image.png)

输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        self.presum_mat = [[0] * (cols + 1) for _ in range(rows + 1)]
        # 构造前缀和：每个矩形[(0,0), (i, j)]之内的元素之和
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.presum_mat[i][j] = (                   # 矩阵前缀和：
                    matrix[i - 1][j - 1]                    # 最小矩形面积
                    + self.presum_mat[i - 1][j]             # 加上上边面积
                    + self.presum_mat[i][j - 1]             # 加上左边面积
                    - self.presum_mat[i - 1][j - 1]         # 减去重复加的
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 区域和 = 三个矩阵的差值（每个矩阵都是以(0,0)为左上角）
        return (
            self.presum_mat[row2 + 1][col2 + 1]             # 最大矩形面积
            - self.presum_mat[row1][col2 + 1]               # 减去上边多余
            - self.presum_mat[row2 + 1][col1]               # 减去左边多余
            + self.presum_mat[row1][col1]                   # 加上重复减的
        )


if __name__ == "__main__":

    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)
    ["","","sumRegion","sumRegion"]
    obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    for sumRegion in [[2,1,4,3],[1,1,2,2],[1,2,2,4]]:
        row1,col1,row2,col2 = sumRegion
        print(obj.sumRegion(row1,col1,row2,col2), end=" ")
    print()
    # [8, 11, 12]
