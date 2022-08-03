num_list = []
odd_num = []

for _ in range(7):
    num = int(input())
    num_list.append(num)

for x in num_list:
    if x % 2 != 0:
        odd_num.append(x)

if len(odd_num) >= 1:
    print(sum(odd_num))
    print(min(odd_num))
else:
    print(-1)