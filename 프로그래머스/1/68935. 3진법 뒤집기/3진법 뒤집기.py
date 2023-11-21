def transform(n, m):
    num = ""
    
    while n > 0:
        n, mod = divmod(n, m)
        num += str(mod)
    
    return num

def solution(n):
    return int(transform(n, 3), 3)