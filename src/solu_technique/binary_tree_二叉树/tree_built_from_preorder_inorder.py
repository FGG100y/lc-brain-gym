"""105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一
棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]
"""
from tree_utils import level_order_bfs, level_order_traversal


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """
    #  可以通过以下步骤构建二叉树：
    #  找到根节点：
    #      在前序遍历中，第一个元素是根节点。
    #      然后在中序遍历中找到该根节点的位置，
    #      根据这个位置可以将中序遍历数组分为左右子树的部分：
    #          根节点左边的部分是左子树。
    #          根节点右边的部分是右子树。
    #  递归构建左右子树：
    #      在中序遍历的左子树部分和右子树部分中，继续构建左右子树。
    #      使用前序遍历的第二个元素（第一个是当前的根）作为新的根节点继续递归。
    #  终止条件：
    #      当中序遍历或前序遍历数组为空时，返回 None，表示当前节点没有子节点。
    """
    def build_tree(self, preorder, inorder):
        # 递归终止条件：没有节点了
        if not preorder or not inorder:
            return None

        # 前序遍历：根-左-右
        # 前序数组的第一个元素就是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 中序遍历：左-根-右
        # 在中序数组中找根节点的位置
        inorder_index = inorder.index(root_val)

        # 构建左右子树
        root.left = self.build_tree(
            preorder[1 : inorder_index + 1], inorder[:inorder_index]
        )
        root.right = self.build_tree(
            preorder[inorder_index + 1 :], inorder[inorder_index + 1 :]
        )

        return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = Solution().build_tree(preorder, inorder)
print(level_order_bfs(root, prt_none=False))
print(level_order_bfs(root, prt_none=True))
print(level_order_traversal(root, prt_none=True))
#  输出: [3,9,20,null,null,15,7]
