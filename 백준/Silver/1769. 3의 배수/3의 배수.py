x = input()

num = x
num_sum = 0
count = 0

if len(x) >= 2:
    while True:
        for i in list(num):
            num_sum += int(i)

        count += 1

        if num_sum < 10:
            if num_sum % 3 == 0:
                print(count)
                print('YES')
            else:
                print(count)
                print('NO')
            break

        num = str(num_sum)
        num_sum = 0
else:
    if int(x) % 3 == 0:
        print(0)
        print('YES')
    else:
        print(0)
        print('NO')