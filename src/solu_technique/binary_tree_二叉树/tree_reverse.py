"""力扣 226. 翻转二叉树
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

示例 2：
输入：root = [2,1,3]
输出：[2,3,1]

示例 3：
输入：root = []
输出：[]
"""

from typing import Optional

from tree_utils import (TreeNode, build_tree, level_order_bfs,
                        level_order_traversal, preorder_traversal)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


if __name__ == "__main__":

    arr = [4, 2, 7, 1, 3, 6, 9]
    root = build_tree(arr)
    new_root = Solution().invertTree(root)
    print("               tree", arr)
    print("      inversed tree", level_order_traversal(new_root))
    print("inversed tree (bfs)", level_order_bfs(new_root))
    print("inversed tree (pre)", preorder_traversal(new_root))
    #  输出：[4,7,2,9,6,3,1]        # level-order
