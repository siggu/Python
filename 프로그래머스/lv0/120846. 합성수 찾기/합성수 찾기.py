def solution(n):
    cnt = 0
    result = 0
    
    if n <= 3:
        return 0
    else:
        for i in range(4, n+1):
            for j in range(1, i+1):
                if i % j == 0:
                    cnt += 1
            if cnt >= 3:
                result += 1
                cnt = 0
            else:
                cnt = 0
    
    return result