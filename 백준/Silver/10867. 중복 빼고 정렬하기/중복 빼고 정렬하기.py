import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr = list(set(arr))
arr.sort()

for x in arr:
    print(x,end=' ')