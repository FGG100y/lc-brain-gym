"""106. 从中序与后序遍历序列构造二叉树
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同
一棵树的后序遍历，请你构造并返回这颗 二叉树 。

示例 1:
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

示例 2:
输入：inorder = [-1], postorder = [-1]
输出：[-1]
"""

from tree_utils import level_order_bfs, level_order_traversal


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    #  可以通过以下步骤构建二叉树：
    #  找到根节点：
    #      在后序遍历中，最后一个元素是根节点。
    #      然后在中序遍历中找到该根节点的位置，
    #      根据这个位置可以将中序遍历数组分为左右子树的部分：
    #          根节点左边的部分是左子树。
    #          根节点右边的部分是右子树。
    #  递归构建左右子树：
    #      在中序遍历的左子树部分和右子树部分中，继续构建左右子树。
    #      使用后序遍历的倒数第二个元素（倒数第一个是当前的根）作为新的根节点继续递归。
    #  终止条件：
    #      当中序遍历或后序遍历数组为空时，返回 None，表示当前节点没有子节点。

    def build_tree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # 后序遍历：左-右-根
        # （递归）传入函数的后序数组的倒数第一个元素就是根节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 中序遍历：左-根-右
        # 在中序数组中找根节点的位置
        inorder_index = inorder.index(root_val)

        # 构建左右子树
        root.left = self.build_tree(inorder[:inorder_index], postorder[:inorder_index])
        root.right = self.build_tree(
            inorder[inorder_index + 1 :], postorder[inorder_index:-1]
        )

        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = Solution().build_tree(inorder, postorder)
print(level_order_bfs(root, prt_none=False))
print(level_order_bfs(root, prt_none=True))
print(level_order_traversal(root, prt_none=True))
#  输出：[3,9,20,null,null,15,7]
