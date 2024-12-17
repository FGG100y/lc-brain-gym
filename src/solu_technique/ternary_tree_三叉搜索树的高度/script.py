"""
题目描述
定义构造三叉搜索树规则如下：

每个节点都存有一个数，当插入一个新的数时，从根节点向下寻找，直到找到一个合适的空节点插入。
查找的规则是：

如果数小于节点的数减去500，则将数插入节点的左子树
如果数大于节点的数加上500，则将数插入节点的右子树
否则，将数插入节点的中子树
给你一系列数，请按以上规则，按顺序将数插入树中，构建出一棵三叉搜索树，最后输出树的高度。

输入描述
第一行为一个数 N，表示有 N 个数，1 ≤ N ≤ 10000

第二行为 N 个空格分隔的整数，每个数的范围为[1,10000]

输出描述
输出树的高度（根节点的高度为1）
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value - 500:
            node.left = self.insert(node.left, value)
        elif value > node.value + 500:
            node.right = self.insert(node.right, value)
        else:
            node.middle = self.insert(node.middle, value)
        return node

    def get_height(self, node):
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        middle_height = self.get_height(node.middle)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, middle_height, right_height)


def run(numbers):

    # 构建三叉搜索树
    tree = TernarySearchTree()
    for num in numbers:
        tree.root = tree.insert(tree.root, num)

    # 输出树的高度
    height = tree.get_height(tree.root)
    print(height)

# 示例用法
if __name__ == "__main__":

    arr = [5000, 2000, 5000, 8000, 1800]                            # 输出 3
    run(arr)

    arr = [5000, 2000, 5000, 8000, 1800, 7500, 4500, 1400, 8100]    # 输出 4
    run(arr)

