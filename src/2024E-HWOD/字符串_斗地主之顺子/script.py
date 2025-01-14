def find_sequence(arr):
    c2n_map = {c:i+11 for i, c in enumerate("JQKA")}
    arr = [int(c2n_map.get(a, a)) for a in arr if a != "2"]
    arr = sorted(set(arr))

    sequences = []
    current_seq = []

    for i in range(len(arr)):
        if not current_seq or arr[i] == current_seq[-1] + 1:
            current_seq.append(arr[i])
        else:
            # 顺子足够长，保存，并开始新的检查
            if len(current_seq) >= 5:
                sequences.append(current_seq)
            current_seq = [arr[i]]

    # 最后一组可能的顺子检查
    if len(current_seq) >= 5:
        sequences.append(current_seq)

    return sequences



arr = list("29J234KA79A56")
assert find_sequence(arr)[0] == [3, 4, 5, 6, 7]
