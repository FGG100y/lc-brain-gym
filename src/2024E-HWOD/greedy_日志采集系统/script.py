def max_score_first_report(logs):
    max_score = float("-inf")

    for i, log in enumerate(logs):
        total_logs = 0
        delay_penalty = 0
        for j in range(i+1):
            total_logs += logs[j]
            delay_penalty += logs[j] * (i - j)
        if total_logs >= 100:
            total_logs = 100  # 达到100条日志，必须上报100条，得分100
            score = total_logs - delay_penalty
            max_score = max(max_score, score)
        # 当前时刻上报得分
        score = total_logs - delay_penalty
        max_score = max(max_score, score)
    return max_score


# 输入处理
raw_in = "3 7 40 10 60"
raw_in = "50 60 1"
raw_in = "1 98 1"
raw_in = "0 0 1"
logs = list(map(int, raw_in.split()))

# 输出首次上报的最大积分
print(max_score_first_report(logs))
