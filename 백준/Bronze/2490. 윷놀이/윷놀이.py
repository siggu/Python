for _ in range(3):
    x = list(map(int, input().split()))
    front = 0

    for i in x:
        if i == 0:
            front += 1

    if front == 1:
        print('A')
    elif front == 2:
        print('B')
    elif front == 3:
        print('C')
    elif front == 4:
        print('D')
    else:
        print('E')