import sys
read = sys.stdin.readline

k, l = map(int, read().rstrip().split())
dic = dict()

for i in range(l):
    student = read().rstrip()
    dic[student] = i
    
dic = sorted(dic.items(), key= lambda x:x[1])

cnt = 0
for i in dic:
    if cnt == k:
        break
    print(i[0])
    cnt += 1