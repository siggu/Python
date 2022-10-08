import sys
read = sys.stdin.readline

N = int(read())
k = 1004000
arr = [False, False] + [True] * k

for i in range(2, int(k ** 0.5) +1):
    if arr[i]:
        for j in range(2*i, k+1, i):
            arr[j] = False

for i in range(N,k+1):
    if arr[i]:
        if str(i) == str(i)[::-1]:
            print(i)
            break