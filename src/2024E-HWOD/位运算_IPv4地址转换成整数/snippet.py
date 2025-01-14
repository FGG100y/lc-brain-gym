def ipaddr_number_conversion(addr, num):
    prefix = "0b"

    # ip -> num
    ip_nums = list(map(int, addr.split(".")))
    bins = "".join([bin(n)[2:].zfill(8) for n in ip_nums])
    the_bin = prefix + bins
    the_num = int(the_bin, 2)
    # num -> ip
    bins = bin(num)[2:].zfill(32) # drop '0b', and fill zeros
    # print(bins)
    nums = []
    size = len(bins) // 4
    # print(len(bins), size)
    i = 0
    while i < len(bins):
        chunk = bins[i:i+size]
        # print(chunk)
        nums.append(int(prefix+chunk, 2))
        i += size
    the_addr = ".".join(list(map(str, nums)))
    return the_num, the_addr



def main():
    addr = input().strip()
    num = int(input().strip())
    result = ipaddr_number_conversion(addr, num)
    for res in result:
        print(res)

main()
