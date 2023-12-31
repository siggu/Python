L = [[0] * 100 for _ in range(100)]

result = 0

for i in range(4):
    l_x, l_y, r_x, r_y = map(int, input().split())

    for j in range(l_x, r_x):
        for z in range(l_y, r_y):
            L[j][z] = 1

for i in L:
    result += i.count(1)

print(result)