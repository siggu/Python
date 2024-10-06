r, c = map(int, input().split())
kayak = [input() for _ in range(r)]
rank = 1
result = [0] * 10

for i in range(c-2, 0, -1):
    flag = 0
    for j in range(r):
        if kayak[j][i] != '.' and result[int(kayak[j][i])] == 0:
            result[int(kayak[j][i])] = rank
            flag = 1
    if flag == 1:
        rank += 1

for i in result:
    if i != 0:
        print(i)