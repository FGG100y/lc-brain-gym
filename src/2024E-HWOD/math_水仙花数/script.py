"""
水仙花数：指一个n位正整数，其各位数字的n次方之和等于该数本身。例如153是1、5、3这三个数字
的立方之和。
输入描述：
第一行输入一个整数，表示一个n位正整数。n取值范围区间为[3,7]。
第二行输入一个正整数m，表示需要返回的第m个水仙花数。如果m大于水仙花数的个数，返回-1
"""
def is_narcissistic(num):
    """判断一个数字是否为水仙花数"""
    digits = list(map(int, str(num)))  # 将数字转换为各位数字的列表
    n = len(digits)
    return sum(d ** n for d in digits) == num

def find_mth_narcissistic(n, m):
    """寻找第m个n位的水仙花数"""
    start = 10**(n-1)  # n位数的起始值
    end = 10**n  # n位数的结束值
    count = 0
    result = []

    # 遍历n位数，判断是否为水仙花数
    for num in range(start, end):
        if is_narcissistic(num):
            result.append(num)
            count += 1
        if count == m:
            return num

    return -1  # 如果m大于水仙花数的个数，返回-1

# 输入
n = int(input())  # 输入的n位正整数
m = int(input())  # 第m个水仙花数

# 输出第m个水仙花数
print(find_mth_narcissistic(n, m))

