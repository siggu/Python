test = int(input())
last_char = []
case_list = []
count = 0
sum = 0

for _ in range(test):
    case = input()

    for x in case:
        case_list.append(x)
    
    for x in case_list:
        last_char.append(x)
        if x == 'O':
            if last_char[0] == 'O':
                count += 1
        else:
            count = 0
        sum += count
        last_char.pop()
    print(sum)
    sum = 0
    count = 0
    case_list = []