import sys
read = sys.stdin.readline

n = int(input())
arr = [float(read().rstrip()) for _ in range(n)]

arr.sort()

for i in range(7):
    print('{:.3f}'.format(arr[i]))