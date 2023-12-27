def solution(n,a,b):
    cnt = 0
    
    while a != b:
        cnt += 1
        a = a//2 + a%2
        b = b//2 + b%2
    
    return cnt