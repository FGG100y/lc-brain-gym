"""
描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数
字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站
的才能出站。
要求输出所有火车出站的方案，以字典序排序输出。
数据范围：1≤n≤10
进阶：时间复杂度：O(n!) ，空间复杂度：O(n)
输入描述：
第一行输入一个正整数N（0 < N <= 10），第二行包括N个正整数，范围为1到10。

输出描述：
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入：
3
1 2 3
输出：
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
说明：
第一种方案：1进、1出、2进、2出、3进、3出
第二种方案：1进、1出、2进、3进、3出、2出
第三种方案：1进、2进、2出、1出、3进、3出
第四种方案：1进、2进、2出、3进、3出、1出
第五种方案：1进、2进、3进、3出、2出、1出
请注意，[3,1,2]这个序列是不可能实现的。
"""
import sys

def train_out_sequences(n, trains):
    def dfs(in_index, stack, out_sequence):
        # 如果所有火车都出站，记录当前方案
        if len(out_sequence) == n:
            result.append(out_sequence[:])
            return

        # 选择入站操作
        if in_index < n:
            stack.append(trains[in_index])          # 火车入站
            dfs(in_index + 1, stack, out_sequence)  # 递归处理下一辆车
            stack.pop()                             # 回溯，撤销入站操作

        # 选择出站操作
        if stack:
            out_sequence.append(stack.pop())        # 栈顶火车出站
            dfs(in_index, stack, out_sequence)      # 递归处理
            stack.append(out_sequence.pop())        # 回溯，撤销出站操作

    result = []
    dfs(0, [], [])

    # 对所有出站方案按字典序排序
    result.sort()

    return result


ins = []
for line in sys.stdin:
    a = line.strip()
    ins.append(a)

n, trains = int(ins[0]), list(map(int, ins[1].split()))
# 获取所有合法的出站方案
sequences = train_out_sequences(n, trains)

# 打印每个出站方案
for seq in sequences:
    print(" ".join(map(str, seq)))
