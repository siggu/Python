def solution(num, total):
    result = []
    
    if num % 2 != 0:
        for i in range(total//num - num//2, total//num + num//2 + 1):
            result.append(i)
    else:
        for i in range(total//num - num//2 + 1, total//num + num//2 + 1):
            result.append(i)
        
    return result