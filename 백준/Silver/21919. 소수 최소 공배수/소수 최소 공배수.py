n = int(input())
a = set(list(map(int, input().split())))

arr = [False, False] + [True] * (max(a)+1)

for i in range(2, max(a)):
    if arr[i]:
        for j in range(i*i, max(a)+1, i):
            arr[j] = False

cnt = 1
for i in a:
    if arr[i]:
        cnt *= i

if cnt == 1:
    print(-1)
else:
    print(cnt)