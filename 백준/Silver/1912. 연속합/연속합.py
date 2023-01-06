import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().rstrip().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] + arr[i - 1])

print(max(arr))