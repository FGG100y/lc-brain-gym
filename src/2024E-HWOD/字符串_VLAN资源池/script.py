""" Vlan是一种为局域网设备进行逻辑划分的技术，为了标识不同的vlan 引入了vlan id 1~4094之
间的整数，定义一个vlan id 的资源池，资源池中连续的vlan用开始vlan-结束vlan表示，不连续的
用单个整数表示，所有的vlan用英文逗号连接起来，现有一个vlan资源池，业务需要从资源池中申请
一个vlan，需要你输出从vlan资源池中移除申请的vlan后的资源池。

输入描述
第一行为字符串格式的vlan资源池
第二行为业务要申请的vlan， vlan的取值范围1~4094

输出描述
从输入vlan资源池中移除申请的vlan后字符串格式的vlan资源池
输出要求满足题目中要求的格式，并且要求从小到大升序输出
如果申请的vlan不在原资源池，输出升序排序的原资源池的字符串即可

示例一
输入
1-5
2
输出
1,3-5
说明：原vlan资源池中有1 2 3 4 5 移除2后
剩下的1 3 4 5按照升序排列的方式为 1 3-5

示例二
输入
20-21,15,18,30,5-10
15
输出
5-10,18,20-21,30
说明：
原vlan资源池中有5 6 7 8 9 10 15 18 20 21 30
移除15后 剩下的为 5 6 7 8 9 10 18 20 21 30
按照题目描述格式并升序后的结果为5-10,18,20-21,30

示例三
输入
5,1-3
10
输出
1-3,5
"""

def parse_vlan_pool(vlan_pool):
    vlans = set()  # 用集合来存储所有VLAN ID
    for part in vlan_pool.split(','):
        if '-' in part:  # 处理范围，例如 "1-5"
            start, end = map(int, part.split('-'))
            vlans.update(range(start, end + 1))
        else:  # 处理单个VLAN，例如 "5"
            vlans.add(int(part))
    return vlans

def format_vlan_pool(vlans):
    vlans = sorted(vlans)
    result = []
    i = 0
    while i < len(vlans):
        start = vlans[i]
        while i + 1 < len(vlans) and vlans[i + 1] == vlans[i] + 1:  # 判断升序连续性
            i += 1
        end = vlans[i]
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")
        i += 1
    return ','.join(result)

def remove_vlan(vlan_pool, apply_vlan):
    vlans = parse_vlan_pool(vlan_pool)
    apply_vlan = int(apply_vlan)

    # 如果申请的VLAN在池中，移除它
    if apply_vlan in vlans:
        vlans.remove(apply_vlan)

    # 重新格式化并返回结果
    return format_vlan_pool(vlans)

# 测试用例
vlan_pool = "20-21,15,18,30,5-10"
apply_vlan = "15"
output = remove_vlan(vlan_pool, apply_vlan)
print(output)  # 输出: 5-10,18,20-21,30

