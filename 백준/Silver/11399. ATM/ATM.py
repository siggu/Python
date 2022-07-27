N = int(input())
P = list(map(int, input().split()))

last_time = 0
time_sum = 0

for _ in range(N):
    min_time = min(P)
    last_time += min_time
    time_sum += last_time
    P.remove(min_time)

print(time_sum)