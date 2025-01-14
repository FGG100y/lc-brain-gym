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

# 初始化变量
is_ok = True  # 表示当前队列头部是否是期望的数据
sz = 0  # 当前队列的大小
cnt = 0  # 需要调整的次数


# 处理 2n 个操作
for i in range(2 * n):
    op = ops[i].split()  # input().split()

    if op[0] == 'remove':
        sz -= 1                 # 队列大小减少
        if not is_ok:
            cnt += 1            # 如果之前需要调整，计数器加一
            is_ok = True        # 重置状态
    else:
        if op[0] == 'head':
            is_ok = (sz == 0)   # 如果队列为空，则新添加的数据就是正确的
        sz += 1                 # 队列大小增加

# 输出结果
print(cnt)
