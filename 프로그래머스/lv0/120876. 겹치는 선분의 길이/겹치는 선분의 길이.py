def solution(lines):
    dic = [set([]) for _ in range(200)]
    cnt = 0
    
    for index, num in enumerate(lines):
        a, b = num
        for i in range(a, b):
            dic[i+100].add(index)
    
    for i in dic:
        if len(i) > 1:
            cnt += 1
    
    return cnt