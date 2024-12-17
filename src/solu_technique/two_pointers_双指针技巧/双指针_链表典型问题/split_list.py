"""力扣第 86 题「分隔链表」
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都
出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

示例 2：
输入：head = [2,1], x = 2
输出：[1,2]

提示：
链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from create_linked_list import ListNode, createLinkedList, prt_linked_list


def partition(head: ListNode, x: int) -> ListNode:
    # 创建两个子链表，最后合并
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    # p1, p2 负责生成子链表
    p1 = dummy1
    p2 = dummy2
    # p 负责遍历原链表
    p = head

    while p:
        if p.val >= x:
            p2.next = p
            p2 = p2.next
        else:
            p1.next = p
            p1 = p1.next
        # 断开原链表每个节点的 next 指针；直接 p=p.next 导致结果链表会有环而出错
        temp = p.next
        p.next = None
        p = temp

    # 合并两个子链表
    p1.next = dummy2.next

    return dummy1.next


head = createLinkedList([1,4,3,2,5,2])
x = 3
newlist = partition(head, x)
prt_linked_list(newlist)        #  [1,2,2,4,3,5]
