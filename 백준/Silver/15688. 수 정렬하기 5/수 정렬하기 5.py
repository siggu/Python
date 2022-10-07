import sys
read = sys.stdin.readline

N = int(read())
arr = []

for _ in range(N):
    num = int(read())
    arr.append(num)

arr.sort()

for i in arr:
    print(i)