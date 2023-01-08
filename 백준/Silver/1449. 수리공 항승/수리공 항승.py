n, l = map(int, input().split())
leak = sorted(list(map(int, input().split())))
idx = 0
cnt = 0

for i in leak:
    if idx < i:
        cnt += 1
        idx = i + l - 1
    
print(cnt)