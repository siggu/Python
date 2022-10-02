import sys
read = sys.stdin.readline

arr = [False, False] + [True]*1000002

for i in range(2, 1000002):
    if arr[i]:
        for j in range(2*i, 1000002, i):
            arr[j] = False

while True:
    n = int(read())
    if n == 0:
        break

    x = n-2
    y = 2

    while y <= x:
        if arr[x] and arr[y]:
            print(f'{n} = {y} + {x}')
            break
        else:
            x -= 1
            y += 1