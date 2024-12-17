
# FIXME 未检查子串长度（不超过s）；更新max_len的逻辑可能有误
def max_even_os(s):
    s2 = s * 2      # 模拟环状，注意边界
    max_len = 0
    window = []
    left = 0

    for right in range(len(s2)):
        num_o = sum(1 for c in window if c == "o")
        if num_o > 2 and num_o % 2 != 0:  # 移动左端直到减去一个“o”
            for i in range(len(window)):
                if window[i] == "o":
                    left += i + 1
                    break
            window = window[left:]
            max_len = max(max_len, right - left + 1)
        window.append(s2[right])

    return max_len


s = "alolobo"
print(max_even_os(s))
