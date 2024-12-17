"""力扣第 21 题「合并两个有序链表」
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：

输入：l1 = [], l2 = []
输出：[]

示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""
from create_linked_list import ListNode, createLinkedList, are_equal #, prt_linked_list

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 创建新链表，可以借助虚拟头节点
    dummy = ListNode(-1)
    p = dummy
    p1 = l1
    p2 = l2

    while p1 is not None and p2 is not None:
        # 比较两个指针，将值较小的接到p指针
        if p1.val > p2.val:
            p.next = p2
            p2 = p2.next
        else:
            p.next = p1
            p1 = p1.next
        p = p.next

    if p1 is not None:  # p1 较长，将剩下的节点接到p后面
        p.next = p1
    if p2 is not None:  # p2 较长，将剩下的节点接到p后面
        p.next = p2

    return dummy.next   # 返回完整链表的目标部分即可


l1 = createLinkedList([])
l1 = createLinkedList([1,2,4])
l2 = createLinkedList([1,3,4,6])
l2 = createLinkedList([])
l2 = createLinkedList([1,6])
l2 = createLinkedList([1,3,4])
newlist = mergeTwoLists(l1, l2)
#  print(prt_linked_list(newlist))
#  assert newlist == createLinkedList([1,1,2,3,4,4])   # linked_list not work like this
assert are_equal(newlist, createLinkedList([1,1,2,3,4,4]))
