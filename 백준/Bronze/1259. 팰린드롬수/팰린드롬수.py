while True:
    n = input()
    reverse_n = []
    count = 1

    if n == '0':
        break

    for _ in n:
        reverse_n.append(n[-count])
        count += 1

    count = 0

    for x in n:
        if x == reverse_n[count]:
            count += 1
            pass

    if count == len(n):
        print('yes')
    else:
        print('no')