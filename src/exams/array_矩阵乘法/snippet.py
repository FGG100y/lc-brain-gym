"""
描述
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这
个矩阵的每个元素是由下面的公式决定的
$$C_{i,j} = \sum^{y-1}_{k=0} A_{ik} * B_{kj}, (0 \le i \le x, 0 \le k \le y)$$
矩阵的大小不超过100*100

输入描述：
第一行包含一个正整数x，代表第一个矩阵的行数
第二行包含一个正整数y，代表第一个矩阵的列数和第二个矩阵的行数
第三行包含一个正整数z，代表第二个矩阵的列数
之后x行，每行y个整数，代表第一个矩阵的值
之后y行，每行z个整数，代表第二个矩阵的值

输出描述：
对于每组输入数据，输出x行，每行z个整数，代表两个矩阵相乘的结果
示例1
输入：
2
3
2
1 2 3
3 2 1
1 2
2 1
3 3
输出：
14 13
10 11
说明：
1 2 3
3 2 1
乘以
1 2
2 1
3 3
等于
14 13
10 11
"""
import sys


def mutiply(A, B):
    if isinstance(A[0], (int, float)):
        # 如果A是一维向量，则将其转换为一个行矩阵
        A = [A]
    if isinstance(B[0], (int, float)):
        # 如果B是一维向量，则将其转换为一个列矩阵
        B = [[b] for b in B]
    x = len(A)
    y = len(A[0])
    z = len(B[0])

    C = [[0 for _ in range(z)] for _ in range(x)]

    for i in range(x):
        for j in range(z):
            for k in range(y):
                C[i][j] += A[i][k] * B[k][j]
    return C

ins = []
for line in sys.stdin:
    if len(line.split()) > 1:
        line = list(map(int, line.strip().split()))
    else:
        line = int(line.strip())
    ins.append(line)

shape = ins[:3]
A_mat = ins[len(shape):len(shape)+shape[0]]
B_mat = ins[len(shape)+shape[0]:]
# print(shape)
# print(A_mat)
# print(B_mat)

prod = mutiply(A_mat, B_mat)
# print(prod)
for row in prod:
    print(" ".join(list(map(str, row))))
