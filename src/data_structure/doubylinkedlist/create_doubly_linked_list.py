"""create DoublyLinkedList"""

class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


def createDoublyLinkedList(arr, verbose=False):
    if not arr:
        return None

    head = DoublyListNode(arr[0])           # 初始化；后续操作是构建并返回完整链表

    cur = head
    for val in arr[1:]:
        new_node = DoublyListNode(val)
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next                      # 将指针移动一位；循环最后是尾结点

    if verbose:
        print(head.val, cur.val)
    return head
