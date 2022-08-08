N = input()
count = 0

if int(N) <= 9:
    N = N + '0'

num_1 = N[0]
num_2 = N[1]

while True:
    plus_num = int(num_1) + int(num_2)
    plus_num = str(plus_num)

    new_num = num_2 + plus_num[-1]

    num_1 = new_num[0]
    num_2 = new_num[1]

    count += 1

    if new_num == N:
        print(count)
        break