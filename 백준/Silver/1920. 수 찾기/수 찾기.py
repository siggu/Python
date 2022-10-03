import sys
read = sys.stdin.readline

N = int(read())
A = set(map(int, read().split()))

M = int(read())
arr = list(map(int, read().split()))

for num in arr:
    print(1) if num in A else print(0)