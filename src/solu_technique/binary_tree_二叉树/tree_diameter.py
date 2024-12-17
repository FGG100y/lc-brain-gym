"""力扣 543. 二叉树的直径
给你一棵二叉树的根节点，返回该树的 直径 。二叉树的 直径 是指树中任意两个节点之间最长路径
的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：
输入：root = [1,2]
输出：1

提示：
树中节点数目在范围 [1, 104] 内
-100 <= Node.val <= 100
"""
from typing import Optional
from tree_utils import TreeNode, build_tree


class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._maxDepth(root)        # 计算深度过程更新直径
        return self.max_diameter

    def _maxDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        # 递归计算左右子树的深度
        left_depth = self._maxDepth(node.left)
        right_depth = self._maxDepth(node.right)
        # 更新最大直径，直径为左右子树深度之和
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)

        # NOTE 递归函数返回的是该节点的最大深度
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":

    arr = [1,2,3,4,5]
    root = build_tree(arr)
    print(Solution().diameterOfBinaryTree(root))
