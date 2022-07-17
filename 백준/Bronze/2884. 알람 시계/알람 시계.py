H, M = map(int, input().split())
    
if M >= 45:
    print(H, end=' ') 
    print(M-45)
else:
    if H - 1 < 0:
        H = 24
    print(H-1, end=' ')
    print(M + 15)
    