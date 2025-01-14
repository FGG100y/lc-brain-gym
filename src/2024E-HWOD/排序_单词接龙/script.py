def cat_words(words, k, n):
    #  单词接龙的规则是：可用于接龙的单词首字母必须要前一个单词的尾字母相同；当存在多个
    #  首字母相同的单词时，取长度最长的单词，如果长度也相等，则取字典序最小的单词；已经
    #  参与接龙的单词不能重复使用。现给定一组全部由小写字母组成单词数组，并指定其中的一
    #  个单词作为起始单词，进行单词接龙，请输出最长的单词串，单词串是单词拼接而成，中间
    #  没有空格。

    result = words[k]
    end_char = result[-1]
    words.pop(k)
    while words:
        candidates = [w for w in words if w[0] == end_char]
        if not candidates:
            break
        cands = sorted(candidates, key=lambda x: len(x))  #, reverse=True)
        to_cats = [w for w in words if len(w) == len(cands[-1])]
        if to_cats:
            cand = sorted(to_cats)[0]
        result += cand
        end_char = result[-1]
        words.remove(cand)
    #  print(result)
    return result


def word_chain(words, k, n):
    result = words[k]
    end_char = result[-1]
    words.pop(k)
    while words:
        candidates = [w for w in words if w[0] == end_char]
        if not candidates:
            break
        # # 一步到位：先按长度降序，再按字典序升序
        cands = sorted(candidates, key=lambda x: (-len(x), x))  #, reverse=True)
        result += cands[0]
        end_char = result[-1]
        words.remove(cands[0])
    return result

k = 0
k = 4
n = 6
words_raw = """
word
dd
da
dc
dword
d
"""
words = words_raw.strip("\n").split("\n")
#  assert cat_words(words, k, n) == "dwordda"
#  assert cat_words(words, k, n) == "worddwordda"
assert word_chain(words, k, n) == "dwordda"
