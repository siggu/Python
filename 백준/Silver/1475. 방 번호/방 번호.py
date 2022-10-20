import sys
read = sys.stdin.readline

N = read().rstrip()
cnt = [0] * 10

for i in N:
    i = int(i)
    if i == 6 or i == 9:
        if cnt[6] <= cnt[9]:
            cnt[6] += 1
        elif cnt[6] > cnt[9]:
            cnt[9] += 1
    else:
        cnt[int(i)] += 1

print(max(cnt))