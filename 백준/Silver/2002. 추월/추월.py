import sys
read = sys.stdin.readline

n = int(read())
cnt = 0

DK = [read().rstrip() for _ in range(n)]
YS = [read().rstrip() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if YS[i] == DK[j]:
            for k in DK[:j]:
                if k in YS[i+1:]:
                    cnt += 1
                    break
    
print(cnt)