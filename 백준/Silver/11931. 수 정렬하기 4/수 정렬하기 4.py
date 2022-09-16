import sys

N = int(sys.stdin.readline())
arr = set()

for _ in range(N):
    num = int(sys.stdin.readline())
    arr.add(num)

arr = list(arr)
arr.sort(reverse=True)

for x in arr:
    print(x)