"""
问题描述
LYA 是一名计算机专业的学生,最近她学习了哈夫曼编码。为了巩固知识,她决定写一个程序来生成哈
夫曼树。
给定一个长度为n 的正整数数组,每个数字代表二叉树叶子节点的权值。请你帮助 LYA 生成一棵哈夫
曼树,并将其按**中序遍历**的顺序输出。
为了保证输出的哈夫曼树唯一,需要满足以下条件:
- 树中每个非叶子节点的权值等于其左右子节点权值之和。
- 对于权值相同的两个节点,左子树的高度应小于等于右子树的高度。
- 在满足上述条件的前提下,左子节点的权值应小于等于右子节点的权值。
输入格式
第一行包含一个正整数
n,表示叶子节点的个数。
第二行包含
n 个正整数,表示每个叶子节点的权值,数值之间用空格分隔。
输出格式
输出一行,包含若干个正整数,表示按中序遍历哈夫曼树得到的节点权值序列,数值之间用空格分
隔。
样例输入
5
5 15 40 30 10
样例输出
40 100 30 60 15 30 5 15 10
"""
import heapq
from tree_utils import inorder_traversal

# 定义节点类
class TreeNode:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    # 为了 heapq 能进行比较，重写 小于 运算符
    def __lt__(self, other):
        return self.weight < other.weight


def huffman_tree(weights):
    heap = []  # 最小堆
    for w in weights:
        heapq.heappush(heap, TreeNode(w))  # 堆中存放TreeNode

    # 迭代合并最小的两个节点
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = TreeNode(left.weight + right.weight, left, right)
        heapq.heappush(heap, new_node)

    # 堆中最后一个节点就是根节点
    root = heapq.heappop(heap)

    return inorder_traversal(root)


n = 5
weights_str = "5 15 40 30 10"
weights = list(map(int, weights_str.split()))
result = huffman_tree(weights)
testcase_str = "40 100 30 60 15 30 5 15 10"
testcase = list(map(int, testcase_str.split()))
assert result == testcase
