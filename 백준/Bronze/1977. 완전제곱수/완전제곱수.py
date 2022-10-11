M = int(input())
N = int(input())

arr = []

for i in range(1, 101):
    if i*i > N:
        break
    if i*i >= M and i*i <= N:
        arr.append(i*i)

if len(arr) >= 1:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)