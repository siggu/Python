import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
tree = list(map(int, read().rstrip().split()))
start, end = 1, sum(tree)

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in tree:
        if i > mid:
            result += i - mid
            if result > M:
                break

    if result >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)  