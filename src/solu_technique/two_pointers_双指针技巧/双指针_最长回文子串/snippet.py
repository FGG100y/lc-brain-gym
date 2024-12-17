import sys

def palindrome(s):
    pals = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            # get mid idx
            mid = len(sub) // 2
            if not len(sub) % 2:  # even
                if sub[:mid] == sub[mid:][::-1]:
                    pals.append(sub)
            else:
                if sub[:mid] == sub[mid+1:][::-1]:
                    pals.append(sub)
    # print(pals)
    return len(sorted(pals, key=len)[-1])





for line in sys.stdin:
    print(palindrome(line.strip()))