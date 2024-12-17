"""力扣第 23 题「合并K个升序链表」
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""
import heapq
from create_linked_list import ListNode, createLinkedList, are_equal, prt_linked_list


def merge_k_lists(lists):
    if not lists:
        return None

    # 虚拟头节点
    dummy = ListNode(-1)
    p = dummy

    h_list = []

    #  # 将k个头节点加入最小堆；
    #  # idx 的作用是：当ListNode没有重载 __lt__() 方法时，heapq在head.val相同时，通过元
    #  组中的idx来决定顺序，否则抛出TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
    #  for i, head in enumerate(lists):
    #      heapq.heappush(h_list, (head.val, i, head))

    #  # 将k个头节点加入最小堆；
    for head in lists:
        if head:
            heapq.heappush(h_list, head)

    while h_list:
        # 获取最小元素
        #  val, i, node = heapq.heappop(h_list)
        node = heapq.heappop(h_list)
        # 接到结果链表中
        p.next = node
        # 将下一个节点添加到最小堆
        if node.next is not None:
            heapq.heappush(h_list, node.next)
            #  heapq.heappush(h_list, (node.next.val, i, node.next))
        p = p.next

    return dummy.next


lists_raw = [[1,4,5],[1,3,4],[2,6]]
lists = [createLinkedList(i) for i in lists_raw]
newlist = merge_k_lists(lists)
prt_linked_list(newlist)        #  [1,1,2,3,4,4,5,6]
