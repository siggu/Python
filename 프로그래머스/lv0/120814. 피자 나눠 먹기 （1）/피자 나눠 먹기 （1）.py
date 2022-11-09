def solution(n):
    cnt = 0
    
    while True:
        if n < 0:
            break
        elif n % 7 == 0:
            return n // 7
        
        n -= 7
        cnt += 1
    
    return cnt