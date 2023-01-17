import sys
read = sys.stdin.readline
k, n = map(int, read().rstrip().split())
arr = [int(read().rstrip()) for _ in range(k)]
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    num = 0
    
    for i in arr:
        num += i // mid
    
    if num >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)