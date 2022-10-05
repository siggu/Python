import sys
read = sys.stdin.readline

k = 123456*2
arr = [False, False] + [True] * (k+1)

a = int(k ** 0.5)

for i in range(2, a+1):
    if arr[i]:
        for j in range(i*i, k+1, i):
            arr[j] = False

while True:
    n = int(read())
    cnt = 0

    if n == 0:
        break

    for i in arr[n+1:2*n+1]:
        if i:
            cnt += 1

    print(cnt)