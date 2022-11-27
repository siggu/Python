a, b = map(str, input().split())
cnt = 0
min_length = 50

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
    exit()
else:
    for i in range(len(b) - len(a)+1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                cnt += 1
        if cnt < min_length:
            min_length = cnt

print(min_length)