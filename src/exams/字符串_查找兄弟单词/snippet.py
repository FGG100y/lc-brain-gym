from collections import Counter

def find_bros(x, candidates, k, verbose=True):
    # bros = set(permutations(x))
    ans = []
    for word in candidates:
        if word == x:
            continue
        for char in word:
            if char not in set(x):
                break
        if Counter(word) == Counter(x):
            ans.append(word)
    ans = sorted(ans)
    if verbose:
        # print(ans)
        print(len(ans))
        if len(ans) >= k:
            print(ans[k-1])
    # return len(ans), ans[k]


def process_input():
    ins = input().strip().split()
    k = int(ins[-1])
    x = ins[-2]
    # print(k, x)
    cands = ins[1:-2]
    find_bros(x, cands, k)

process_input()