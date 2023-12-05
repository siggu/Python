def solution(n):
    """
    5000 2500 1250 625 624 312 156 78 39 38 14 7 6 3 2 1 0
    N 부터 2로 계속 나누다가
    나눌 수 없는 순간 1을 빼주고
    result += 1 해준다.
    """
    result = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            result += 1
            n -= 1
    
    return result