def solution(sides):
    cnt = 0
    max_num = max(sides)
    min_num = min(sides)
    
    for i in range(max_num-min_num+1, max_num+1):
        cnt += 1
    
    for i in range(max_num+1, max_num+min_num):
        cnt += 1
    
    return cnt
    