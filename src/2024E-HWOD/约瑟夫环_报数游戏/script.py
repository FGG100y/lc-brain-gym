def josephus_problem(M, N=100):
    if M <= 1 or M >= N:
        return "ERROR!"

    people = list(range(1, N+1))

    index = 0  # 起始索引
    while len(people) >= M:
        index = (index + M - 1) % len(people)  # % for circulating
        people.pop(index)

    return sorted(people)

M = 2
#  73
assert josephus_problem(M) == [73]

M = 3
#  58,91
assert josephus_problem(M) == [58, 91]

M = 4
#  34,45,97
assert josephus_problem(M) == [34, 45, 97]

for i in range(2, 10):
    print(f"M={i}", josephus_problem(i))
