def solution(a, b, n):
    result = 0

    while a <= n:
        result += (n // a) * b
        
        n = (n % a) + (n // a) * b
        
    return result
    
