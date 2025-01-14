def find_secret_number(n, guesses):
    # 从所有候选数字中过滤不符合提示的候选者
    candidates = [str(i).zfill(4) for i in range(10000)]

    for guess, hint in guesses:
        guess_str = str(guess).zfill(4)
        x, y = map(int, hint.replace("A", " ").replace("B", "").split())
        # 过滤不符合提示的候选
        candidates = [
            cand for cand in candidates if calculate_score(guess_str, cand) == (x, y)
        ]

        if not candidates:
            return "NA"

    return candidates[0] if len(candidates) == 1 else "NA"


def calculate_score(guess, answer):
    a_cnt = sum(1 for i in range(4) if guess[i] == answer[i])  # A 位置、数字都正确
    # B 数字正确而位置不对的数的个数; NOTE answer 其实是指传入的 candidate
    b_cnt = sum(min(guess.count(d), answer.count(d)) for d in set(guess)) - a_cnt
    return a_cnt, b_cnt


n = 6
guesses_raw = """
4815 1A1B
5716 0A1B
7842 0A1B
4901 0A0B
8585 3A0B
8555 2A1B
"""
guesses = [elem.split() for elem in guesses_raw.strip("\n").split("\n")]
assert "3585" == find_secret_number(n, guesses)  # test success
assert "5585" == find_secret_number(n, guesses)  # would failed
