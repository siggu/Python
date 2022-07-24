N = input()
sort_num = []

for x in N:
    sort_num.append(x)
  
sort_num.sort(reverse=True)
print(''.join(sort_num))