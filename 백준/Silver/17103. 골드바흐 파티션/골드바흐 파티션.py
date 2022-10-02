import sys
read = sys.stdin.readline

arr = [False, False] + [True]*1000002

for i in range(2, 1000002):
    if arr[i]:
        for j in range(2*i, 1000002, i):
            arr[j] = False

n = int(read())

for _ in range(n):
    num = int(read())
    cnt = 0

    for i in range(2, int(num/2) + 1):
        if arr[i] and arr[num-i]:
            cnt += 1

    print(cnt)