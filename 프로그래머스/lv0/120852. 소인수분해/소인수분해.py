def solution(n):
    result = []
    
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)
    
    for i in result:
        for j in range(2, 10000):
            if i * j in result:
                result.remove(i*j)
    
    result.sort()
    return result 
