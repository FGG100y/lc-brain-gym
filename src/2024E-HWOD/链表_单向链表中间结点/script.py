"""
题目描述：给定一个单链表L，编写程序输出L中间结点保存的数据（如果有两个，输出第二个的）。
输入描述：
每个输入包含一个测试用例，每个测试用例：第一行给出首结点地址和结点总数N（N≤105）。结点地
址为5位非负整数，NULL用-1表示。
接下来N行，每行格式为：”Address Data Next"
"""
def find_middle_node(start, n, nodes):
    """找到链表的中间节点（如果有两个，返回第二个）"""
    linked_list = []
    current = start

    # 遍历链表，构建顺序链表
    while current != "-1":
        linked_list.append(current)
        current = nodes[current][1]  # 访问下一节点

    # 获取中间节点的索引
    middle_index = len(linked_list) // 2  # 偶数时输出第二个中间节点

    # 输出中间节点的数据
    middle_node = linked_list[middle_index]
    return nodes[middle_node][0]  # 返回中间节点保存的数据


# 输入
start, n = input().split()  # 读取首结点地址和节点总数
n = int(n)

# 读取链表信息，并使用字典进行保存数据：{地址指针: (数据，下一个结点)}
nodes = {}
for _ in range(n):
    address, data, next_node = input().split()
    nodes[address] = (data, next_node)

# 输出中间节点的数据
print(find_middle_node(start, n, nodes))

