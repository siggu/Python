n = int(input())
degree = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in degree:
    result += i[0] * i[1]

print(result)