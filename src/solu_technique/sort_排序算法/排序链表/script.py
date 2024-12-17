"""148 排序链表

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]


「147. 对链表进行插入排序」要求使用插入排序的方法对链表进行排序，插入排序的时间复杂度是
O(n^2)，其中 n 是链表的长度。这道题考虑时间复杂度更低的排序算法。题目的进阶问题要求达到
O(nlogn) 的时间复杂度和 O(1) 的空间复杂度，时间复杂度是 O(nlogn) 的排序算法包括归并排序、
堆排序和快速排序（快速排序的最差时间复杂度是 O(n^2)），其中最适合链表的排序算法是归并排
序。

归并排序基于分治算法。最容易想到的实现方式是自顶向下的递归实现，考虑到递归调用的栈空间，
自顶向下归并排序的空间复杂度是 O(logn)。如果要达到 O(1) 的空间复杂度，则需要使用自底向上
的实现方式。
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# merge sort 对链表进行排序
def sort_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    mid = _find_mid_node(head)                  # find_mid_node将链表一分为二

    left = sort_list(head)                      # head代表左半部分
    right = sort_list(mid)                      # mid 代表右半部分
    return _merge(left, right)

def _find_mid_node(head):
    # 快慢指针
    slow, fast = head, head
    left_nodes = None
    while fast and fast.next:                   # 忽略 fast.next 则 AttributeError
        left_nodes = slow
        slow = slow.next
        fast = fast.next.next
    left_nodes.next = None                      # 将传入链表截断，分为两部分
    return slow

def _merge(left, right):
    # a dummy head needed? Yes.
    dummy = ListNode(-1)
    dummy_head = dummy
    while left and right:
        if left.val < right.val:
            dummy_head.next = left
            left = left.next
        else:
            dummy_head.next = right
            right = right.next
        dummy_head = dummy_head.next
    dummy_head.next = left if left else right
    return dummy.next

# 插入排序
def insertion_sort_list(head):                  # 仅仅出于好奇这个 O(n^2) 算法细节
    dummy = ListNode(-1)
    current = head
    while current:
        # 在已排序链表中找到插入位置
        prev = dummy                                    # 指向已排序链表的最后一个节点
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        # 插入当前节点到已排序链表
        next_temp = current.next                        # 保存下一个要处理的节点
        current.next = prev.next                        # 将当前节点插入到prev之后
        prev.next = current                             # 更新已排序链表的下一个节点
        current = next_temp                             # 继续处理下一个节点
    return dummy.next


# 创建一个链表 4 -> 2 -> 1 -> 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))   # 注意ListNode的定义
#  sorted_head = insertion_sort_list(head)
sorted_head = sort_list(head)
# 打印排序后的链表
current = sorted_head
while current:
    print(current.val, end=" -> ")
    current = current.next  # 输出: 1 -> 2 -> 3 -> 4 ->
print()                     # 在命令行另起一行
