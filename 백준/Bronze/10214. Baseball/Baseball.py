for _ in range(int(input())):
    
    ans = "Draw"
    
    Yonsei = 0
    Korea = 0
    
    for _ in range(9):
        y, k = map(int, input().split())
        Yonsei += y
        Korea += k
        
    if Yonsei > Korea:
        ans = "Yonsei"
    elif Yonsei < Korea:
        ans = "Korea"
            
    print(ans)