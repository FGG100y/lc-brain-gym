def longest_substring_of_numbers(s):
    # sliding window
    results = []
    max_len = 0

    digits = set("1,2,3,4,5,6,7,8,9,0".split(","))
    for i, char in enumerate(s):
        if char in digits:
            start = i
            while i < len(s) and s[i] in digits:
                i += 1
            cur_window = s[start:i]
            if len(cur_window) > max_len:
                max_len = len(cur_window)
                results = [cur_window]
            elif len(cur_window) == max_len:
                results.append(cur_window)
        else:
            i += 1
    return "".join(results), max_len


#  def main():
#      try:
#          while True:
#              ins = input().strip().splitlines()
#              if not ins:
#                  break
#              for s in ins:
#                  nums, maxlen = longest_substring_of_numbers(s)
#                  print(f"{nums},{maxlen}")
#      except EOFError:
#          pass

s_raw = """
abcd12345ed125ss123058789
a8a72a6a5yy98y65ee1r2
"""
seqs = s_raw.strip("\n").splitlines()
#  print(seqs)
for s in seqs:
    nums, maxlen = longest_substring_of_numbers(s)
    print(f"{nums},{maxlen}")
