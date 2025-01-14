class Node:
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
            return Node(value)
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

def main():
    # 输入
    #  N = int(input())  # 数的个数
    #  numbers = list(map(int, input().split()))  # 数的列表
    N = 5
    numbers = [5000, 2000, 5000, 8000, 1800]

    # 构建三叉搜索树
    tree = TernarySearchTree()
    for num in numbers:
        tree.root = tree.insert(tree.root, num)

    # 输出树的高度
    height = tree.get_height(tree.root)
    print(height)

# 示例用法
if __name__ == "__main__":
    main()

