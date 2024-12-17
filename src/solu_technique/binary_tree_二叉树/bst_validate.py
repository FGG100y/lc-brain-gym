"""98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

- 节点的左子树只包含 小于 当前节点的数。
- 节点的右子树只包含 大于 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

输入：root = [2,1,3]
输出：true

输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""

from tree_utils import TreeNode, build_tree

# 二叉搜索树（BST）：root的整个左子树都要小于root.val，整个右子树都要大于root.val


class SolutionRecursive:
    """DFS"""
    def is_valid_bst(self, root: TreeNode) -> bool:

        def validate(node, low=float("-inf"), high=float("inf")):
            # base case：空节点是合法的BST
            if node is None:
                return True

            # 如果 node.val 不满足 min_val, max_val 的限制，则不是bst
            if node.val <= low or node.val >= high:
                return False

            # 限定左子树的最大值是root.val，右子树的最小值是root.val
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root)


class SolutionIterative:
    """
    若是BST，则其中序遍历结果是严格递增的序列，因此可以在遍历中检查节点值是否是递增顺序
    """
    def is_valid_bst(self, root: TreeNode) -> bool:
        stack = []
        inorder = float("-inf")         # 记录上一个访问的节点值

        #  中序遍历（左-根-右）
        while stack or root:
            # 一直向左走，将节点压入栈中
            while root:
                stack.append(root)
                root = root.left

            # 栈顶元素（后进先出）
            root = stack.pop()
            if root.val <= inorder:     # 当前节点值小于等于上一个节点值，则不是BST
                return False
            inorder = root.val          # 更新上一个节点值

            # 继续处理右子树
            root = root.right

        return True


arr = [2, 1, 3]
arr = [5, 1, 4, None, None, 3, 6]
root = build_tree(arr)

print(arr)
print(SolutionRecursive().is_valid_bst(root))
print(SolutionIterative().is_valid_bst(root))
