def freq_num(lst):
    count = {}
    for n in lst:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    most = min([num for num, freq in count.items() if freq == max(count.values())])
    return most
    
def long_seq(lst):
    max_len = 0
    cur_len = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1
    max_len = max(max_len, cur_len)
    return max_len
    
    
n1 = [1, 3, 5, 4, 1, 1]
n2 = [5, 3, 5, 4, 4, 1]

print(freq_num(n1))
print(freq_num(n2))

n3 = [1, 2, 3, 4, 4, 2, 2, 2]
n4 = [1, 2, 3, 4, 5]

print(long_seq(n3))
print(long_seq(n4))
