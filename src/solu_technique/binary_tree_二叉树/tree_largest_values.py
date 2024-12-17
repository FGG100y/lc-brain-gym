"""力扣 515. 在每个树行中找最大值
定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]

示例2：
输入: root = [1,2,3]
输出: [1,3]
"""
from collections import deque
from typing import Optional
from tree_utils import TreeNode, build_tree, level_order_traversal


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        # BFS
        if root is None:
            return []
        result = []
        queue = deque([root])

        while queue:
            level_sz = len(queue)                   # 当前层的节点数
            level_max = float("-inf")
            for _ in range(level_sz):               # 遍历当前层所有节点
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result


if __name__ == "__main__":

    arr = [1,3,2,5,3,None,9]
    root = build_tree(arr)
    print(Solution().largestValues(root))
    #  输出: [1,3,9]
