"""LeetCode 253: Meeting Rooms II:

Given an array of meeting time intervals where intervals[i] = [start_i, end_i], find the
minimum number of conference rooms required to host all meetings.

Key Insights:
To solve this problem, we need to determine how many meetings overlap at any given time.
Each overlap indicates the need for an additional room.
"""
#  Two-Pointer Technique:
#
#  Use two pointers: one for iterating over the sorted start times and the other for the
#  end times.
#  Traverse through the start times. If a meeting starts before the earliest current
#  meeting ends, a new room is required.
#  If a meeting ends before the next meeting starts, a room is freed.

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # 开始时刻和结束时刻
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    # 初始化参数
    start_prt, end_prt = 0, 0
    rooms_needed = 0
    max_rooms = 0

    # 遍历整个数组
    while start_prt < len(intervals):
        # 当前会议没结束，就有会议要开始，增加会议室；查看下一个开始时间
        if starts[start_prt] < ends[end_prt]:
            rooms_needed += 1
            start_prt += 1
        else:   # 否则空出会议室；查看下一个结束时间
            rooms_needed -= 1
            end_prt += 1

        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms


intervals = [[0, 30], [5, 10], [15, 20]]
print(min_meeting_rooms(intervals))  # Output: 2
