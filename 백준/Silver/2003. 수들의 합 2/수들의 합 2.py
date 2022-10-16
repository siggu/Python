import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
A = list(map(int, read().rstrip().split()))

start  = 0
end = 1
cnt = 0
num_sum = A[0]

while True:
    if num_sum < M:
        if end < N:
            num_sum += A[end]
            end += 1
        else:
            break
    elif num_sum == M:
        cnt += 1
        num_sum -= A[start]
        start += 1
    else:
        num_sum -= A[start]
        start += 1

print(cnt)