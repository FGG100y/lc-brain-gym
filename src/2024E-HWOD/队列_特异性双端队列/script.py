"""
最小的调整次数
问题描述
有一个特异性的双端队列，该队列可以从头部或尾部添加数据，但是只能从头部移出数据。

K小姐 依次执行2n 个指令往队列中添加数据和移出数据。其中n 个指令是添加数据（可能从头部添
加、也可能从尾部添加），依次添加1 到n；n 个指令是移出数据。

现在要求移除数据的顺序为1 n。

为了满足最后输出的要求，K小姐 可以在任何时候调整队列中数据的顺序。

请问K小姐 最少需要调整几次才能够满足移除数据的顺序正好是1 到n。

输入格式
第一行一个整数n，表示数据的范围。

接下来的2n 行，其中有n 行为添加数据，指令为：

"head add x" 表示从头部添加数据x
"tail add x" 表示从尾部添加数据x
另外n 行为移出数据指令，指令为 "remove" 的形式，表示移出1 个数据。

输出格式
输出一个整数，表示K小姐要调整的最小次数。

样例输入
5
head add 1
tail add 2
remove
head add 3
tail add 4
head add 5
remove
remove
remove
remove
样例输出
1
"""

from collections import deque

def min_adjustments(operations):
    queue = deque()  # 用deque模拟双端队列
    remove_order = 1  # 当前期望移除的元素
    adjustments = 0  # 记录调整次数

    for op in operations:
        if op.startswith("head add"):
            # 从头部添加
            x = op.split()[-1]
            queue.appendleft(int(x))
        elif op.startswith("tail add"):
            # 从尾部添加
            x = op.split()[-1]
            queue.append(int(x))
        elif queue and op == "remove":
            #  print(queue)
            #  breakpoint()
            # 检查队列头部是否为期望的移除顺序
            if queue[0] != remove_order:
                # 需要调整，将目标元素移动到头部
                #  queue.remove(remove_order)
                sort_l = sorted(queue)
                queue = deque(sort_l)
                adjustments += 1
            # 移除队列头部元素
            queue.popleft()
            remove_order += 1

    return adjustments

#  # 输入处理
#  n = int(input())
#  operations = [input().strip() for _ in range(2 * n)]


n = 5  # int(input())
ops_raw = """
tail add 1
head add 2
remove
head add 3
tail add 4
remove
head add 5
remove
remove
remove
"""
ops = ops_raw.strip("\n").splitlines()
#  print(ops)
#  breakpoint()

# 输出最小调整次数
print(min_adjustments(ops))

