"""
将格式为 {1～128} #{0~255}#{0~255}#{0~255}的ipv4地址(即#分割的4节的ipv4形式)转换为对应的
32位整数，输入形式为字符串，存在空串、含ip中不存在的字符、非合法的#分十进制数、十进制数
不在合法区间 的4种非法输入，此时输出“invalid ip"（100分）

样例1: 100#101#1#5
输出: 1684340997
样例2: 1#2#3
输出: invalid ip
"""
def convert_int_to_ip(num, sep="."):
    """将32位整数转换为IP地址"""
    try:
        if not (0 <= num <= 0xFFFFFFFF):  # 检查整数是否在合法范围内
            return "invalid ip"

        # 通过位运算提取每一段的IP
        part1 = (num >> 24) & 255
        part2 = (num >> 16) & 255
        part3 = (num >> 8) & 255
        part4 = num & 255

        # 格式化为 sep 分割的IP字符串
        return f"{part1}{sep}{part2}{sep}{part3}{sep}{part4}"

    except Exception:
        return "invalid ip"


def convert_ip_to_int(ip_str):
    try:
        # 检查空字符串
        if not ip_str:
            return "invalid ip"

        # 以 # 分割IP字符串
        parts = ip_str.split("#")

        # 检查是否为四段
        if len(parts) != 4:
            return "invalid ip"

        # 转换每一段并检查合法性
        ip_parts = []
        for part in parts:
            # 检查是否为数字
            if not part.isdigit():      # FIXME “01”.isdigit() -> True, which make this buggy
                return "invalid ip"

            num = int(part)

            # 检查是否在合法范围内
            if num < 0 or num > 255:
                return "invalid ip"

            ip_parts.append(num)

        # 计算32位整数： (第1段 << 24) | (第2段 << 16) | (第3段 << 8) | 第4段
        ip_int = (ip_parts[0] << 24) | (ip_parts[1] << 16) | (ip_parts[2] << 8) | ip_parts[3]

        return ip_int

    except Exception:
        return "invalid ip"

#  # 输入
#  ip_str = input("输入IP地址（#分隔形式）或32位整数：")
#
#  # 判断输入类型
#  if "#" in ip_str:
#      # 将IP地址转换为整数
#      result = convert_ip_to_int(ip_str)
#  else:
#      try:
#          # 将字符串转换为整数
#          ip_int = int(ip_str)
#          result = convert_int_to_ip(ip_int)
#      except ValueError:
#          result = "invalid ip"
#
#  # 输出结果
#  print(result)

# 输入
ip_str = "100#101#1#5"  #input()
ip_str = "10#0#3#193"   # 167773121
ip_num = 167773121
# 输出转换结果
print(convert_ip_to_int(ip_str))
print(convert_int_to_ip(ip_num, sep="#"))
