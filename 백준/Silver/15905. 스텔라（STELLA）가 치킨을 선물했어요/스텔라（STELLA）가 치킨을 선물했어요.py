n = int(input())

result = []
cnt = 0

for _ in range(n):
    result.append(list(map(int, input().split())))
    
result.sort(key=lambda x : (x[0], x[1]), reverse=True)

compare = result[4][0]

for i in range(5, n):
    if result[i][0] == compare:
        cnt += 1

print(cnt)