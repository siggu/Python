p, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0

while True:
    for i in a:
        if p >= 200:
            break
        # print(f'p = {p}')
        p += i
        cnt += 1
    break

print(cnt)