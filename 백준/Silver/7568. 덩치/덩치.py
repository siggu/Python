n = int(input())
deongchi = []

for _ in range(n):
    deongchi.append(list(map(int, input().split())))

rank = [1] * n

for x in range(n):
    for y in range(n):
        if deongchi[x][0] < deongchi[y][0] and deongchi[x][1] < deongchi[y][1]:
            rank[x] += 1

for z in rank:
    print(z, end=" ")