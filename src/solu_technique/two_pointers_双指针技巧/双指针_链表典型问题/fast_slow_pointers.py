"""力扣 876. 链表的中间结点
给你单链表的头结点 head ，请你找出并返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

示例 1：
输入：head = [1,2,3,4,5]
输出：[3,4,5]
解释：链表只有一个中间结点，值为 3 。

示例 2：
输入：head = [1,2,3,4,5,6]
输出：[4,5,6]
解释：该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。

提示：
链表的结点数范围是 [1, 100]
1 <= Node.val <= 100
"""
from create_linked_list import ListNode, createLinkedList, createCycleList, prt_linked_list


#  class ListNode:
#      def __init__(self, x):
#          self.val = x
#          self.next = None
#
#      # 方便将 ListNode 进行比较
#      def __lt__(self, other):
#          return self.val < other.val

def middel_node(head: ListNode) -> ListNode:
    # 快慢指针
    # 快指针每次走两步，慢指针只走一步
    # 前者到终点时，后者到中点
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


head = createLinkedList([1,2,3,4,5,6])
head = createLinkedList([1,2,3,4,5])
newlist = middel_node(head)
prt_linked_list(newlist)            #  [3,4,5]


def has_cycle(head: ListNode) -> bool:
    # 快慢指针
    # 快指针每次走两步，慢指针只走一步
    # 如果快指针与慢指针相遇，则必有环 （环会导致无限循环遍历，快的终究会追上慢的）
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

head = createLinkedList([1,2,3,4,5,6])
headc = createCycleList(head, 3)
#  prt_linked_list(headc)               # 无限循环
print(has_cycle(headc))


def detect_cycle(head: ListNode) -> ListNode:
    """如果有环，找出环的起始节点"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    # 快慢指针相遇后，让其中一个指针指向头节点，
    # 然后使两个指针以**相同速度**前进，则再次相遇的节点就是环的起点
    slow = head
    #  idx = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        #  idx += 1
    #  return idx           # 3
    #  return slow.val      # 4
    return slow

print(detect_cycle(headc))


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    """找到并返回两条链表的相交点，否则返回None"""
    p1, p2 = headA, headB
    while p1 != p2:
        # p1 走到A链表末尾，转到B链表
        # p2 走到B链表末尾，转到A链表
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1

