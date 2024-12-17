"""create LinkedList"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # 方便将 ListNode 进行比较
    def __lt__(self, other):
        return self.val < other.val

def createLinkedList(arr, verbose=False):
    if not arr:
        return None

    head = ListNode(arr[0])                 # 初始化；后续操作是构建并返回完整链表

    cur = head
    for val in arr[1:]:
        new_node = ListNode(val)
        cur.next = new_node
        cur = cur.next                      # 将指针移动一位；循环最后是尾结点

    if verbose:
        print(head.val, cur.val)
    return head

def createCycleList(head: ListNode, cycle_start_pos: int) -> ListNode:
    if not head or cycle_start_pos < 0:
        return head  # No cycle to create

    current = head
    cycle_start_node = None
    index = 0

    # Traverse the linked list to find the cycle start node and the end node
    while current.next:
        if index == cycle_start_pos:
            cycle_start_node = current  # Store the cycle start node
        current = current.next
        index += 1

    # If the cycle start node is defined, create the cycle
    if cycle_start_node:
        current.next = cycle_start_node  # Create the cycle

    return head  # Return the head of the modified list

def create_intersect_list(head: ListNode, cycle_start_pos: int) -> ListNode:
    pass


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


def prt_linked_list(head):
    ans = []
    curr = head
    while curr is not None:
        ans.append(curr.val)
        #  print(curr.val, end=" ")
        curr = curr.next
    #  print()
    ans_fmt =  ",".join(map(str, ans))
    print(f"[{ans_fmt}]")


def are_equal(list1, list2):
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1, list2 = list1.next, list2.next
    return list1 is None and list2 is None

