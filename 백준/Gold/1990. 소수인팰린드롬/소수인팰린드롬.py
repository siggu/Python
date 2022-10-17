import sys
read = sys.stdin.readline

a, b = map(int, read().rstrip().split())

if b > 10000000:
    b = 10000000

arr = [False, False] + [True] * b

for i in range(2, int(b**0.5) + 1):
    if arr[i]:
        for j in range(2*i, b+1, i):
            arr[j] = False

for i in range(a, b+1):
    if arr[i]:
        i = str(i)
        if i == i[::-1]:
            print(i)

print(-1)