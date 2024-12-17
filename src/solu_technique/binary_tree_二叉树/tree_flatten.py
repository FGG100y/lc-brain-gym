"""114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针
始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]
"""
from tree_utils import TreeNode, build_tree

#  class TreeNode:
#      def __init__(self, val=0):
#          self.val = val
#          self.left = None
#          self.right = None


class SolutionRecursive:
    """
    递归解法：
    - 对每个节点，先展平其左右子树
    - 将展平后的左子树插入到右子树的位置，原本的右子树连接到左子树的末端
    - 继续递归处理数的其他节点
    """
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        # 递归展开左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序位置操作
        # 保存右子树
        right_subtree = root.right
        # 左子树放到右子树位置
        root.right = root.left
        root.left = None
        # 找到当前右子树（之前的左子树）的末端
        current = root
        while current.right:
            current = current.right
        # 将原右子树接到末端
        current.right = right_subtree


class SolutionIterative:
    """
    迭代解法
    通过右节点的遍历，将左子树移到右侧。迭代式将当前左子树移到右子树的位置。
    """
    def flatten(self, root: TreeNode) -> None:
        current = root
        while current:
            if current.left:
                # 找到左子树的最右节点
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                # 将右子树接到左子树的最右节点的右侧
                rightmost.right = current.right
                # 再将左子树移到右侧
                current.right = current.left
                current.left = None

            # 继续处理下一个节点
            current = current.right



if __name__ == "__main__":

    root_arr = [1,2,5,3,4,None,6]
    root = build_tree(root_arr)

    recursive = True
    recursive = False
    if recursive:
        SolutionRecursive().flatten(root)
    else:
        SolutionIterative().flatten(root)
    head = root
    while head:
        print(head.val, end=" ")
        head = head.right
    print()
    #  输出：[1,null,2,null,3,null,4,null,5,null,6]
