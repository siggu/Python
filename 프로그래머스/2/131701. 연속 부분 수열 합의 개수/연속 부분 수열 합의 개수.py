def solution(elements):
    L = elements*2
    result = []
    cnt = 0
    
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            result.append(sum(L[cnt:i+cnt]))
            cnt += 1
        cnt = 0
    
    return len(list(set(result)))