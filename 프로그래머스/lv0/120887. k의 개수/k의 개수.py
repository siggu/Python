def solution(i, j, k):
    cnt = 0
    
    for x in range(i, j+1):
        if str(k) in str(x):
            # print(x)
            cnt += str(x).count(str(k))
    
    return cnt