N, X = map(int, input().split())

A = map(int, input().split())
 
for x in A:
    if x < X:
        print(x,end=' ')