import sys
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

arr = A + B

arr.sort()

for x in arr:
    print(x,end=" ")