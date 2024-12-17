from data_structure import DoublyListNode, createDoublyLinkedList


def prt_linkedlist():
    node = linkedlist
    while node is not None:
        if node.next is None:
            print(node.val)
        else:
            print(node.val, end=" ")
        node = node.next


# 创建一个双链表
arr = [1, 2, 3, 4, 5,]
linkedlist = createDoublyLinkedList(arr, verbose=False)
#  breakpoint()

# 在双链表尾部插入新元素
# ----------------------
# 先将指针移到最后一个节点
tail = linkedlist
while tail.next is not None:
    tail = tail.next

# 在双链表尾部更新指针（插入新元素）
new_node = DoublyListNode(6)
tail.next = new_node
new_node.prev = tail
tail = new_node

prt_linkedlist()

# 继续在尾部添加新元素
new_node = DoublyListNode(6)
tail.next = new_node
new_node.prev = tail
tail = new_node

prt_linkedlist()

# 也就是说，如果已经维护一个tail节点，那么每次在链表尾部添加新元素就不需要重复遍历链表。


# 在双链表中间插入新元素
# ----------------------
# 在第3个节点后面插入新节点
p = linkedlist                  # p指向链表的head，即第一个节点
for _ in range(2):              # 两次next就到达第三个节点
    p = p.next

# 组装新节点
new_node = DoublyListNode(77)
new_node.next = p.next
new_node.prev = p

# 插入新节点
p.next.prev = new_node
p.next = new_node

prt_linkedlist()

# 在双链表中间删除节点
# --------------------

# 删除第四个节点
# 先找到第三个节点
p = linkedlist
for _ in range(2):
    p = p.next

to_del = p.next
p.next = to_del.next
to_del.next.prev = p

# 清理 to_del 节点
to_del.next = None
to_del.prev = None

prt_linkedlist()
