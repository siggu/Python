import sys
read = sys.stdin.readline

N = int(input().rstrip())
first = list(map(int,input().split()))

M = int(input().rstrip())
second = list(map(int,input().split()))

dict = {}

for i in first:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for j in second:
    if j in dict:
        print(dict[j],end=' ')
    else:
        print(0, end=' ')