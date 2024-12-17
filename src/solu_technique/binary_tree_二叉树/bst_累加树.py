class Solution:
    def accumualte_tree(self, root, k):
        res = [0]  # 使用列表是因为在 Python 中需要在递归函数中更新外部变量

        def traverse(node):     # 降序遍历BST完成累加树需求
            if not node:
                return

            # 从右子树开始遍历
            traverse(node.right)

            # 中序位置:维护累加和
            res[0] += node.val
            node.val = res[0]

            traverse(node.left)

        # 调用递归遍历
        traverse(root)
        return res[0]

