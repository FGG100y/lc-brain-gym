def can_get_attendance_award(record):
    # absent 不超过1次: record.count("absent") > 1 -> false
    # 没有: 连续的 late/leaveearly: record[i] and record[i-1] == late/leaveearly
    # 任意连续7次考勤，absent/late/leaveearly 不超过3次: slide window=7

    win_size = 7

    if record.count("absent") > 1:
        return False

    for i in range(1, len(record)):
        if (record[i] == "late" and record[i - 1] == "late") or (
            record[i] == "leaveearly" and record[i - 1] == "leaveearly"
        ):
            return False

    for i in range(len(record) - win_size + 1):
        window = record[i : i + win_size]
        bad_records = (
            window.count("absent") + window.count("late") + window.count("leaveearly")
        )
        if bad_records >= 3:
            return False

    return True


record = "present absent present present leaveearly present absent".split()
record = "present present present leaveearly present absent".split()
record = "present present present present present leaveearly leaveearly present absent".split()
record = "present present present present present leaveearly present leaveearly present absent".split()
print("true" if can_get_attendance_award(record) else "false")
