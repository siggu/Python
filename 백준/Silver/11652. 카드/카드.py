import sys
read = sys.stdin.readline
dic = {}
n = int(read().rstrip())

for _ in range(n):
    card = int(read().rstrip())
    
    if card in dic:
        dic[card] +=1
    else:
        dic[card] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])