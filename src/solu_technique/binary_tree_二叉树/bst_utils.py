#  from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # 节点值
        self.left = left      # 左子节点
        self.right = right    # 右子节点

class BST:
    def __init__(self):
        self.root = None      # 初始化时树为空

    def insert(self, val: int) -> None:
        """插入一个新值到二叉搜索树中，跳过None。"""
        if not self.root:
            self.root = TreeNode(val)  # 如果树为空，则新节点成为根节点
        else:
            self._insert_recursive(self.root, val)  # 否则递归插入

    def _insert_recursive(self, node: TreeNode, val: int) -> None:
        """递归插入新值。"""
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)  # 如果左子节点为空，插入新节点
            else:
                self._insert_recursive(node.left, val)  # 否则递归左子树
        else:
            if node.right is None:
                node.right = TreeNode(val)  # 如果右子节点为空，插入新节点
            else:
                self._insert_recursive(node.right, val)  # 否则递归右子树


def build_bst(arr):
    # 示例用法
    bst = BST()
    for value in arr:
        if value:
            bst.insert(value)
    return bst.root


if __name__ == "__main__":
    from tree_utils import inorder_traversal

    values = [7, 3, 9, 1, 5, 8, 10]  # 要插入的节点值
    root = build_bst(values)
    print("中序遍历 BST 的结果：")
    inorder_traversal(root)  # 输出结果应该是：1 3 5 7 8 9 10
    print()

