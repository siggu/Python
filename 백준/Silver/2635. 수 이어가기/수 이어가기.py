first = int(input())

result_list = []
len_list = 0

for i in range(1, first+1):
    num_list = []
    num_list.append(first)
    num_list.append(i)
    idx = 0
    while True:
        check_num = num_list[idx] - num_list[idx+1]
        idx += 1
        
        if check_num < 0:
            break
        else:
            num_list.append(check_num)
        
        if len_list < len(num_list):
            len_list = len(num_list)
            result_list = num_list[:]

print(len(result_list))
print(*result_list)