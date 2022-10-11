N, K = list(map(int, input().split()))

arr = []

for i in range(1, N+1):
    if len(arr) == K:
        break
    if N % i == 0:
        arr.append(i)

if len(arr) < K:
    print(0)
else:
    print(arr[-1])