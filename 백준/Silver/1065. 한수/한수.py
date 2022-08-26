N = int(input())
count = 0

while True:
    if N <= 99:
        print(N)
        break

    N = str(N)

    for x in range(100, int(N)+1):
        x = str(x)

        if int(x[0]) - int(x[1]) == int(x[1]) - int(x[2]):
            count += 1

    print(count + 99)
    break