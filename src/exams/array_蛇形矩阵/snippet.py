def matrix_snade(N, verbose=True):
     # 初始化首行和之后每行的加和因子
    result = [[sum(range(i+1)) for i in range(1, N+1)]]
    adds = list(range(1, N))

    n = N -1
    # 生成每行的数据
    for i in range(n, 0, -1):  # 从n到1倒序，因为第一行有n个元素
        row = []
        for j in range(i):
            val = result[n-i][j] + adds[j]
            row.append(val)
        adds = adds[1:]
        result.append(row)
    
    if verbose:
        # 打印结果
        for row in result:
            print(" ".join(map(str, row)))


def main():
    N = int(input().strip())
    matrix_snade(N, verbose=True)
main()