"""力扣 230. 二叉搜索树中第 K 小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素
（从 1 开始计数）。

示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何
优化算法？
"""
from bst_utils import build_bst
from tree_utils import inorder_traversal


class Solution:
    def __init__(self):
        self.ans = 0
        self.rank = 0

    #  def kth_smallest_recursive(self, root, k):        # 必须遍历整棵树（其实没必要）
    #      return inorder_traversal(root)[k-1]

    def kth_smallest_recursive(self, root, k):
        # 记录结果和当前排名
        res = [0]  # 使用列表是因为在 Python 中需要在递归函数中更新外部变量
        rank = [0]  # 同样使用列表来传递和更新排名

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            # 中序遍历代码位置
            rank[0] += 1
            if rank[0] == k:
                res[0] = node.val
                return
            traverse(node.right)

        # 调用递归遍历
        traverse(root)
        return res[0]

    def kth_smallest_iterative(self, bst, k):
        # bst 中序遍历结果是升序排序
        stack = []
        current = root
        rank = 0

        # 中序遍历（左-根-右）
        while stack or current:
            # 先遍历到最左子节点
            while current:
                stack.append(current)
                current = current.left
            # 弹出栈顶元素，当前中序遍历到最小元素
            current = stack.pop()
            rank += 1

            # 如果已经找到第k小元素，返回其值
            if rank == k:
                return current.val

            # 继续遍历右子树
            current = current.right

k = 3
arr = [5,5,3,6,2,4,None,None,1]
root = build_bst(arr)
#  print(inorder_traversal(root))

print(Solution().kth_smallest_recursive(root, k))
print(Solution().kth_smallest_iterative(root, k))
#  输出：3
