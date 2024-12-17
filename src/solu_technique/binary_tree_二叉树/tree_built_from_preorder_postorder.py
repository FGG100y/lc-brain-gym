"""889 根据前序和后序遍历构造二叉树
给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前
序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 任何 一个。



示例 1：
输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]

示例 2:
输入: preorder = [1], postorder = [1]
输出: [1]
"""

from tree_utils import level_order_bfs, level_order_traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    构建的过程比较复杂，因为前序遍历和后序遍历不能直接区分左右子树的边界。具体思路如下：

    根节点：
        前序遍历的第一个元素是根节点，后序遍历的最后一个元素是根节点。

    左子树的根节点：
        前序遍历的第二个元素是左子树的根节点。根据这个节点在后序遍历中的位置，我们可以知
        道左子树的大小，进而划分出前序遍历和后序遍历中的左右子树部分。

    递归构建左右子树：
        确定了左子树的范围后，递归构建左右子树，直到数组为空时，返回 None 表示没有子节点。
    """

    def build_tree(self, preorder, postorder):
        # 如果前序遍历为空，返回None
        if not preorder or not postorder:
            return None

        # 前序遍历的第一个节点是根节点
        root = TreeNode(preorder[0])

        # 如果只有一个节点，直接返回根节点
        if len(preorder) == 1:
            return root

        # 前序遍历的第二个节点是左子树的根节点，找到它在后序遍历中的位置
        left_root_val = preorder[1]
        left_subtree_size = postorder.index(left_root_val) + 1

        # 递归构建左子树和右子树
        root.left = self.build_tree(
            preorder[1 : 1 + left_subtree_size], postorder[:left_subtree_size]
        )
        root.right = self.build_tree(
            preorder[1 + left_subtree_size :], postorder[left_subtree_size:-1]
        )

        return root


preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
root = Solution().build_tree(preorder, postorder)
print(level_order_bfs(root, prt_none=False))
print(level_order_bfs(root, prt_none=True))
print(level_order_traversal(root, prt_none=True))
#  输出：[1,2,3,4,5,6,7]
