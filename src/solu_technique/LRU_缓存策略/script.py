"""力扣第 146 题「LRU缓存机制」
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，
则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最
久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。



示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""

# hashmap + doublyLinkedList

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()                         # 存放的是{key: node}
        self.size = 0
        # 使用虚拟头尾节点，并组建
        self.dummy_head = DLinkedNode()
        self.dummy_tail = DLinkedNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 拿到节点
        node = self.cache[key]
        # 要送到双链表头部，表示最近使用
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 变更值，移送头部
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            # 不存在的，就新建节点，也要移送头部
            new_node = DLinkedNode(key, value)
            # 添加到字典
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # 如果超过承载量，删除尾部键值对
            self.size += 1
            if self.size > self.capacity:
                # 删除双链表尾部节点，从字典删除
                removed = self._remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1

    # 操作链表头尾节点；注意拼接顺序

    def _add_to_head(self, node):
        node.prev = self.dummy_head
        node.next = self.dummy_head.next
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        node = self.dummy_tail.prev
        self._remove_node(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lRUCache = LRUCache(2)
print(lRUCache.put(1, 1))
print(lRUCache.put(2, 2))
print(lRUCache.get(1))
print(lRUCache.put(3, 3))
print(lRUCache.get(2))
print(lRUCache.put(4, 4))
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
