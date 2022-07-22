N = int(input())
count = 0

while True:
    if N % 5 == 0:
        N = N - 5
    elif N % 3 == 0 and N % 5 != 0:
        N = N - 3
    elif N / 5 >= 1:
        N = N - 5
    elif N / 3 >= 1:
        N = N - 3
    else:
        print(-1)
        break
    count += 1
    if N == 0:
        print(count)
        break
