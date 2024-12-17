"""leetcode 61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

def create_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        new_node = ListNode(val)
        cur.next = new_node
        cur = cur.next
    return head

def prt_linkedlist(head):
    curr = head
    #  while curr:
    #      print(curr.val, end="->")
    #      curr = curr.next
    #  print()
    #  return
    while curr is not None:
        # 打印成一行（屏幕小，还分窗格:'）
        if curr.next is None:
            print(curr.val)
        else:
            print(curr.val, end=" ")
        curr = curr.next


class Solution:

    def __init__(self):
        self.successor = None

    # 递归翻转单链表
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        last = self.reverse(head.next)          # 递归
        head.next.next = head                   # 翻转指向
        head.next = None                        # 尾节点处理
        return last

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverse_between(self, head, m, n):
        if m == 1:
            return self.reverseN(head, n)
        # 不明觉厉（但很费空间复杂度）
        head.next = self.reverse_between(head.next, m-1, n-1)
        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 与字符串单词翻转思路类似
        # 全翻转+部分翻转

        m = 0
        cur = head
        while cur is not None:
            m += 1
            cur = cur.next

        k %= m
        node = self.reverseN(head, m-k)
        node = self.reverse(node)
        node = self.reverseN(node, k)
        return node

arr = [1,2,3,4,5]
#  arr = [0,1,2]
head = create_linkedlist(arr)
prt_linkedlist(head)
#  node = Solution().reverse(head)
#  prt_linkedlist(node)
#  node = Solution().reverseN(node, n=2)
#  prt_linkedlist(node)
#  breakpoint()
#  node = Solution().reverse_between(head, 2, 4)
#  prt_linkedlist(node)

node = Solution().rotateRight(head, k=4)
prt_linkedlist(node)
