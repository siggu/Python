import sys
input = sys.stdin.readline

n = int(input())
arr1 = [False, False] + [True]*(n-1)
arr2 = []

for i in range(2, int(n**0.5)+1):
    if arr1:
        arr1[i*2::i] = [False]*((n-i)//i)

for i in range(n+1):
    if arr1[i] == True:
        arr2.append(i)

cnt, result = 0, 0
i,j = 0,0
while(True):
    if result == n:
        cnt+=1
        
    if result > n:
        result -= arr2[i]
        i+=1
    elif j == len(arr2):
        break
    else:
        result += arr2[j]
        j+=1
        
print(cnt)