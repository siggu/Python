import sys
read = sys.stdin.readline

N = int(read())
result = 0

for i in range(1, N+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == N):                 
        result = i                   
        break

print(result)