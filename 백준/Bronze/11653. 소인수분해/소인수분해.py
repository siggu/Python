N = int(input())
count = 2

while True:
    if N == 1:
        break
    elif N % count == 0:
        print(count)
        N = N / count
    else:
        count += 1