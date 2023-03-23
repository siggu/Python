n = int(input())
m = int(input())
arr = sorted(list(map(int,input().split())))
cnt = 0
i, j = 0, n-1

while i < j:
    if arr[i] + arr[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] < m:
        i += 1
    else:
        j -= 1

print(cnt)