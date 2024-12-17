from collections import deque


# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root


# ----------------------
# 前、中、后序遍历二叉树
# ----------------------

# 前序遍历：根 -> 左 -> 右
def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# 中序遍历：左 -> 根 -> 右
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# 后序遍历：左 -> 右 -> 根
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

# 层次遍历：按层打印节点，可选保留 None 来表示空节点
def level_order_traversal(root, prt_none=False):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            if prt_none:               # 保留None到打印结果中
                result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)     # 左子节点
            queue.append(node.right)    # 右子节点

    if prt_none:
        # 清理结果列表末尾多余的 None
        while result and result[-1] is None:
            result.pop()

    return result


# 层序遍历“标准”做法（带for循环）：处理逻辑更清晰
def level_order_bfs(root, prt_none=False):
    if root is None:
        return []
    result = []
    queue = deque([root])

    while queue:
        level_sz = len(queue)                   # 当前层的节点数
        level_nodes = []
        for _ in range(level_sz):               # 遍历当前层所有节点
            node = queue.popleft()
            if node is not None:
                level_nodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                if prt_none:
                    level_nodes.append(None)
        result.extend(level_nodes)

    if prt_none:
        # 清理结果列表末尾多余的 None
        while result and result[-1] is None:
            result.pop()

    return result



if __name__ == "__main__":
    arr = [3,9,20,None,None,15,7]
    #  arr = [1,None,2]
    root = build_tree(arr)

    print("前序遍历:", preorder_traversal(root))
    print("中序遍历:", inorder_traversal(root))
    print("后序遍历:", postorder_traversal(root))

    #  # 示例树构建函数
    #  root = TreeNode(3)
    #  root.left = TreeNode(9)
    #  root.right = TreeNode(20)
    #  root.right.left = TreeNode(15)
    #  root.right.right = TreeNode(7)

    print("层次遍历（BFS）:", level_order_bfs(root))
    # 打印包含 None 的层次遍历
    print("层次遍历（包含 None）:", level_order_traversal(root, with_none=True))

