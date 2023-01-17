n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort(key=lambda x:(x[1],x[0]))

cnt = 0
last = 0

for i, j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)