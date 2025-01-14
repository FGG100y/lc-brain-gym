"""报文响应时间
问题描述
IGMP（Internet Group Management Protocol）协议中有一个字段称为最大响应时间（Max Response
Time）。当主机（HOST）收到查询报文时，会解析出 MaxResponseTime 字段，并在(0,
MaxResponseTime] 时间（秒）内选取一个随机时间来回应一个响应报文。如果在这个随机时间内收
到一个新的查询报文，则会根据两者时间的大小，选取较小的一方来刷新回应时间。

0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+
|1| exp | mant |
+-+-+-+-+-+-+-+-+
最大响应时间的计算方式如下：

当Max Resp Code<128 时，Max Resp Time=Max Resp Code；
Max Resp Code≥128 时，Max Resp Time=(mant∣0x10)<<(exp+3)；
其中，exp exp 为最大响应时间的高 5~7 位，mant mant 为最大响应时间的低 4 位。
注意：接收到的MaxRespCode MaxRespCode 最大值为 255，所有字段均为无符号数。

现在假设 HOST 收到查询报文时，选取的随机时间必定为最大值。给定 HOST 收到的查询报文个数C，
每个查询报文的接收时间T 和最大响应时间字段值M，请计算出 HOST 发送响应报文的时间。

输入格式
第一行为查询报文个数C。 后续每行包含两个整数，分别为 HOST 收到报文时间T 和最大响应时间M，
以空格分隔。

输出格式
输出一个整数，表示 HOST 发送响应报文的时间。

样例输入
3
0 20
1 10
8 20
样例输出
11
样例解释
收到 3 个报文：

第 0 秒收到第 1 个报文，响应时间为 20 秒，则要到
0+20=20 秒响应；

第 1 秒收到第 2 个报文，响应时间为 10 秒，则要到
1+10=11 秒响应，与上面的报文的响应时间比较获得响应时间最小为 11 秒；

第 8 秒收到第 3 个报文，响应时间为 20 秒，则要到
8+20=28 秒响应，与上面的报文的响应时间比较获得响应时间最小为 11 秒；
最终得到最小响应报文时间为 11 秒。

样例输入
2
0 255
200 60
样例输出
260
样例解释
收到 2 个报文：

第 0 秒收到第 1 个报文，响应时间为 255 秒，则要到(15∣0x10)<<(7+3)=31744 秒响应；(
mant=15，exp=7)
第 200 秒收到第 2 个报文，响应时间为 60 秒，则要到200+60=260 秒响应，与上面的报文的响应
时间比较获得响应时间最小为 260 秒；最终得到最小响应报文时间为 260 秒。
"""
def calculate_max_response_time(C, messages):
    min_response_time = float('inf')

    for T, M in messages:
        if M < 128:
            MaxRespTime = M
        else:
            # 解析 exp 和 mant
            exp = (M >> 4) & 0b111  # 高 5-7 位
            mant = M & 0b1111       # 低 4 位
            MaxRespTime = (mant | 0x10) << (exp + 3)

        # 计算响应时间
        response_time = T + MaxRespTime
        min_response_time = min(min_response_time, response_time)

    return min_response_time

#  # 输入读取
#  C = int(input())
#  messages = [tuple(map(int, input().split())) for _ in range(C)]

C = 2
msg_raw = """
0 255
200 60
"""
messages = [tuple(map(int, line.split())) for line in msg_raw.strip("\n").splitlines()]
# 输出最小的响应时间
print(calculate_max_response_time(C, messages))

