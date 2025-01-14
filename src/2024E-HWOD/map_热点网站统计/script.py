"""
题目
企业路由器的统计页面，有一个功能需要动态的统计公司访问最多的网页URL top N。

输入描述：每一行都是一个URL或一个数字，如果是URL，代表一段时间内的网页访问；如果是一个数
字N，代表本次需要输出的Top N个URL。
输入约束：
1、总访问网页数量小于5000个，单网页访问次数小于65535次；
2、网页URL仅由字母，数字和点分隔符组成，且长度小于等于127字节；
3、数字是正整数，小于等于10且小于当期总访问网页数。

输出描述：每行输入要对应一行输出，输出按访问次数排序的前N个URL，用逗号分隔。
输出要求：
1、每次输出要统计之前所有输入，不仅是本次输入；
2、如果访问次数相等的URL，按URL的字符串字典序升序排列，输出排序靠前的URL。

示例2：
输入：
news.qq.com
www.cctv.com
1
www.huawei.com
www.huawei.com
2
3
输出：
news.qq.com
www.huawei.com,news.qq.com
www.huawei.com,news.qq.com,www.cctv.com
"""
from collections import defaultdict

def process_input(inputs):
    # 记录URL及其访问次数的字典
    url_count = defaultdict(int)

    for line in inputs:
        if line.isdigit():
            # 如果是数字，表示要输出 Top N
            N = int(line)
            # 对字典按访问次数降序，字典序升序排序
            sorted_urls = sorted(url_count.items(), key=lambda x: (-x[1], x[0]))
            # 提取前 N 个 URL
            top_n_urls = [url for url, count in sorted_urls[:N]]
            # 输出按逗号分隔的 Top N URL
            print(",".join(top_n_urls))
        else:
            # 如果是 URL，记录该 URL 的访问次数
            url_count[line] += 1

# 输入数据
inputs = [
    "news.qq.com",
    "www.cctv.com",
    "1",
    "www.huawei.com",
    "www.huawei.com",
    "2",
    "3"
]

# 处理输入并输出结果
process_input(inputs)

