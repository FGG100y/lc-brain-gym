
def api_kwcount(urls, query, verbose=False):
    # 构建字典
    res = {}
    kw_d = {}
    for url in urls.strip().split("\n"):
        if not url:
            continue
        url_items = url.strip()[1:].split('/')
        for i in range(len(url_items)):
            level = i + 1
            kw = url_items[i]
            if kw in kw_d:
                kw_d[kw] += 1
            else:
                kw_d[kw] = 1
            res[level] = {kw: kw_d[kw]}
    idx, kw = query  # e.g., (2, "computing")

    if verbose:
        print(res)

    if res.get(int(idx), -1) < 0:
        return 0
    return res[int(idx)].get(kw, 0)


n = 5
urls = """
/huawei/computing/no/one
/huawei/computing
/huawei
/huawei/cloud/no/one
/huawei/wireless/no/one
"""
query = (2, "computing")
query = (1, "huawei")
query = (4, "two")
query = (6, "one")
print(api_kwcount(urls, query))
