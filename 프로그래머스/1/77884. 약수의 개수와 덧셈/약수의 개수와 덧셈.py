def solution(left, right):
    result = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i):
            if i % j == 0:
                cnt += 1
        print(cnt)
        if cnt % 2 == 0:
            result -= i
        else:
            result += i
    
    return result