import sys
read = sys.stdin.readline

n = int(read())
dic = {}

for i in range(2*n - 1):
    name = read().rstrip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 0

for j in dic:
    if dic[j] % 2 == 0:
        print(j)
        break