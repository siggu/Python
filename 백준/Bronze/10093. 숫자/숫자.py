A, B = map(int, input().split())

if B > A:
    print(B - A - 1)

    for x in range(A+1, B):
        print(x,end=' ')

elif A > B:
    print(A - B - 1)
    
    for y in range(B+1, A):
        print(y, end=' ')
        
elif A == B:
    print(0)