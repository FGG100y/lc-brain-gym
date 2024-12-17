"""力扣第 19 题「删除链表的倒数第 N 个结点」
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

进阶：你能尝试使用一趟扫描实现吗？
"""
from create_linked_list import ListNode, createLinkedList, are_equal, prt_linked_list


#  使用了虚拟头结点的技巧，是为了防止出现空指针的情况，比如说链表总共有 5 个节点，题目
#  就让你删除倒数第 5 个节点，也就是第一个节点，那按照算法逻辑，应该首先找到倒数第 6 个
#  节点。但第一个节点前面已经没有节点了，这就会出错。
#  但有了虚拟节点 dummy 的存在，就避免了这个问题，能够对这种情况进行正确的删除。
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    # 虚拟头结点
    dummy = ListNode(-1)
    dummy.next = head

    # 删除倒数第n个节点，要先找到倒数第n+1这个节点
    x = find_from_end(dummy, n+1)
    # 删除第n个节点：
    x.next = x.next.next

    return dummy.next

def find_from_end(head, k):
    # 双指针，一个先走k步，再一起走完，
    # 则后走的指针刚好指向(len(head)-k+1)这个节点，就是倒数第k个节点
    p1, p2 = head, head
    for _ in range(k):
        p1 = p1.next
    while p1 is not None:
        p2 = p2.next
        p1 = p1.next
    return p2


n = 1
arr = [2]
n = 2
arr = [1,2,3,4,5]
head = createLinkedList(arr)
newlist = remove_nth_from_end(head, n)
prt_linked_list(newlist)                #  [1,2,3,5]
