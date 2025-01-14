"""
题目描述：荒岛逃生游戏。岛上有若干人，需要向两端港口逃生，假定每个人移动速度一样，且只可
以选择向左或向右逃生。如果两人相遇，则进行决斗，战斗力值高的活下来，并损失掉与对方相同的
战斗力；如果战斗力相等则两人同归于尽。逃生方向相同的人永不发生决斗。
输入描述：
输入非0整数数组，正负表示逃生方向，负向左，正向右，值表示战斗力；并且越左边的数字表示
距离左边港口越近。
输出描述：
能够逃生的人的总数，没有人逃生输出0，输入一场输出-1。
示例：
输入: ”5 10 8 -8 -5“，
输出: 2.
"""


def escape_game(arr):
    # 使用栈来保存向右逃生的人，遇到向左的则进行决斗（如果根本没有向右的，则保存向左的）
    if not arr or 0 in arr:
        return -1

    stack = []

    for person in arr:  # 模拟决斗
        if person > 0:
            stack.append(person)                # 设定：向右逃的人入栈
        else:                                   # 处理向左逃的人
            while stack and stack[-1] > 0:
                if stack[-1] + person == 0:
                    stack.pop()
                    break
                elif stack[-1] + person > 0:
                    stack[-1] += person
                    break
                else:                           # 向左逃生赢，战斗继续
                    person += stack[-1]
                    stack.pop()
            else:
                stack.append(person)            # 没有遇到决斗的人

    return len(stack)


arr_raw = "5 10 8 -8 -5"
arr_raw = "-7 -2 -3"
arr_raw = "7 2 3 -12"
arr_raw = "-7 2 3 -12"
arr_raw = "5 10 8 -8 -5 2 -7"
arr_raw = "5 10 8 -8 -5 -7 2"
arr_raw = "0 5 10 8 -8 -5 -7 2"
arr = list(map(int, arr_raw.split()))
print(escape_game(arr))
