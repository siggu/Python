n, m = map(int, input().split())
s = input()
words = [input() for _ in range(m)]
result = []
idx = 0
cnt = 0

for i in range(m):
    for j in words[i]:
        if j == s[idx]:
            idx += 1
            cnt += 1
        if idx >= n:
            break
    
    if cnt >= n:
        result.append('true')
    else:
        result.append('false')
    idx = 0
    cnt = 0

for i in result:
    print(i)