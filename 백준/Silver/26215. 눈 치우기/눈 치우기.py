n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
time = 0
time_out = False

for _ in range(len(a)):
    # print(f'a = {a}')
    if len(a) >= 2:
        a[0] = a[0] - a[1]
        # print(f'a = {a}')
        time += a[1]
        a.remove(a[1])
        a.sort(reverse=True)
    else:
        time += a[0]

if time >= 1441:
    print(-1)
else:
    print(time)