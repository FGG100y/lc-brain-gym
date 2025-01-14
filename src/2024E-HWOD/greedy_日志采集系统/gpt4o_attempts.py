#  # Second attempt of GPT4o, still failed:
#  def max_score_first_report(logs):
#      total_logs = 0  # 累积日志条数
#      delay_penalty = 0  # 延迟罚分
#      max_score = float('-inf')  # 初始化最大积分
#
#      # 遍历每个时刻的日志数
#      for i, log in enumerate(logs):
#          total_logs += log
#          delay_penalty += total_logs  # 计算当前时刻所有日志的延迟罚分
#
#          # 如果日志数达到或超过100条，必须上报
#          if total_logs >= 100:
#              # 只允许上报100条日志，计算积分
#              score = 100 - delay_penalty + total_logs - 100  # 上报100条，并扣除延迟时间的罚分
#              max_score = max(max_score, score)
#              break
#
#          # 否则，计算当前时刻上报的积分
#          score = total_logs - delay_penalty
#          max_score = max(max_score, score)
#
#      return max_score


#  # Third attempt of GPT4o, after explain the penalty rule:
def max_score_first_report(logs):
    total_logs = 0  # 累积日志条数
    max_score = float('-inf')  # 初始化最大积分

    # 遍历每个时刻的日志数
    for i in range(len(logs)):
        total_logs = 0  # 初始化累积日志数
        delay_penalty = 0  # 延迟罚分

        # 累积到当前时刻的日志数，并计算延迟罚分
        for j in range(i + 1):
            total_logs += logs[j]  # 累积日志数
            delay_penalty += logs[j] * (i - j)  # 延迟秒数乘以该时刻的日志数

        # 如果日志数达到或超过100条，必须上报
        if total_logs >= 100:
            total_logs = 100  # 强制最多上报100条
            score = total_logs - delay_penalty
            max_score = max(max_score, score)
            break

        # 计算当前时刻上报的积分
        score = total_logs - delay_penalty
        max_score = max(max_score, score)

    return max_score


# 输入处理
logs = list(map(int, "3 7 40 10 60".split()))

# 输出首次上报的最大积分
print(max_score_first_report(logs))

