"""力扣第 104 题「二叉树的最大深度」
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2

提示：
树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100
"""
from typing import Optional
from tree_utils import TreeNode, build_tree

class Solution1:
    def __init__(self):
        self.res = 0
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self._traverse(root)
        return self.res

    def _traverse(self, root):                              # 遍历计算思路
        if root is None:
            return
        # 前序位置（进入节点）
        self.depth += 1                                     # 深度加一
        if (root.left is None and root.right is None):      # 到达叶子节点
            self.res = max(self.res, self.depth)            # 更新最大深度
        # 递归
        self._traverse(root.left)
        self._traverse(root.right)
        # 后序位置（离开节点）
        self.depth -= 1                                     # 深度减一

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:    # 分解问题计算思路
        if root is None:
            return 0
        # 左右子树分别递归，求最大深度
        left_depth = self.maxDepth(root.left)               # 递归左子树
        right_depth = self.maxDepth(root.right)             # 递归右子树
        return max(left_depth, right_depth) + 1             # 最深子树加一（根结点）


if __name__ == "__main__":

    arr = [3,9,20,None,None,15,7]
    root = build_tree(arr)
    print(Solution1().maxDepth(root))
    print(Solution2().maxDepth(root))
    #  输出：3
