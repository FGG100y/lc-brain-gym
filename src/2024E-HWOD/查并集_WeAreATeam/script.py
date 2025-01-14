"""We Are A Team题目描述
总共有n个人在机房，每个人有一个标号(1<=标号<=n)，他们分成了多个团队，需要你根据收到的m条
消息判定指定的两个人是否在一个团队中，具体的:

1.消息构成为abc，整数a、b分别代表两个人的标号，整数c代表指令

2.c==0代表a和b在一个团队内

3.c==1代表需要判定a和b的关系，如果a和b是一个团队，输出一行’we are a team’,如果不是，输出
    一行'we are not a team'

4.c为其他值，或当前行a或b超出1~n的范围，输出da pian zi

输入描述

1.第一行包含两个整数n，m(1<=n,m<100000),分别表示有n个人和m条消息

2.随后的m行，每行一条消息，消息格式为:abc(1<=a,b<=n,0<=c<=1)

输出描述

1.c==1,根据a和b是否在一个团队中输出一行字符串，在一个团队中输出we are a team不在一个团队
    中输出'we are not a team'

2.c为其他值，或当前行a或b的标号小于1或者大于n时，输出字符串da pian zi

3.如果第一行n和m的值超出约定的范围时，输出字符串”Null“。

示例1
输入
5 6
1 2 0
1 2 1
1 5 0
2 3 1
2 5 1
1 3 2
输出
we are a team
we are not a team
we are a team
da pian zi

示例2
输入
5 7
1 2 0
4 5 0
2 3 0
1 2 1
2 3 1
4 5 1
1 5 1
输出
we are a team
we are a team
we are a team
we are not a team
"""

#  这道题目可以使用并查集（Union-Find）来处理。并查集是一种常用的数据结构，主要用于处理
#  动态连通性问题。它支持两种操作：
#
#  - 合并操作（Union）：将两个元素所在的集合合并为一个。
#  - 查找操作（Find）：查找某个元素所在的集合的标识（根节点），用来判断两个元素是否属于
#    同一个集合。

# 并查集实现
class UnionFind:
    def __init__(self, n):
        # 初始化父节点，每个人的父节点都是自己
        self.parent = list(range(n + 1))
        # 初始化每个人的秩为1
        self.rank = [1] * (n + 1)

    # 查找操作，带路径压缩
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 合并操作，按秩合并
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # 将秩小的树合并到秩大的树上
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def process_messages(n, m, messages):
    if not (1 <= n <= 100000 and 1 <= m <= 100000):
        return ["NULL"]

    uf = UnionFind(n)
    result = []

    for msg in messages:
        a, b, c = msg

        # 检查边界条件
        if not (1 <= a <= n and 1 <= b <= n and c in [0, 1]):
            result.append("da pian zi")
            continue

        if c == 0:
            # 合并 a 和 b 所属的团队
            uf.union(a, b)
        elif c == 1:
            # 判断 a 和 b 是否在一个团队
            if uf.find(a) == uf.find(b):
                result.append("we are a team")
            else:
                result.append("we are not a team")

    return result


# 读取输入并处理

n, m = 5, 7
messages_raw ="""
1 2 0
4 5 0
2 3 0
1 2 1
2 3 1
4 5 1
1 5 1
"""
messages = [list(map(int, line.split())) for line in messages_raw.strip("\n").splitlines()]

output ="""
we are a team
we are a team
we are a team
we are not a team
"""

#  n, m = map(int, input().split())
#  messages = [list(map(int, input().split())) for _ in range(m)]
result = process_messages(n, m, messages)
print("\n".join(result))

