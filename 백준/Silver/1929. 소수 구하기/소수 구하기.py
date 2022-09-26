import sys
read = sys.stdin.readline
n, m = map(int, read().split())

arr = [True] * (m + 1)

k = int(m ** 0.5)

for i in range(2, k+1):
    if arr[i] == True:
        for j in range(i*i, m+1, i):
            arr[j] = False

for i in range(n, m+1):
    if i == 1:
        pass
    elif arr[i]:
        print(i)