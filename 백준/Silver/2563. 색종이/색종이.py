L = [[0]*100 for _ in range(100)]

n = int(input())
result = 0

for i in range(n):
    x, y = map(int, input().split())

    # 3, 7 -> 13, 17까지
    for j in range(x, x+10):
        for z in range(y, y+10):
            L[j][z] = 1

for i in L:
    result += i.count(1)

print(result)