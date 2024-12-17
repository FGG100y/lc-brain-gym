"""LeetCode 79:
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回
true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直
相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


def exist(board, word) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(i, j, index):
        # 如果已经匹配到单词最后一个字符，返回True
        if index == len(word):
            return True
        # 边界检查以及当前字符匹配检查
        if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[index]:
            return False

        temp = board[i][j]
        board[i][j] = "#"

        found = (
            dfs(i + 1, j, index + 1)
            or dfs(i - 1, j, index + 1)
            or dfs(i, j + 1, index + 1)
            or dfs(i, j - 1, index + 1)
        )

        board[i][j] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))
