def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    cnt = 0
    result = 0
    
    for i in babbling:
        for j in word:
            if j in i:
                i = i.replace(j, '_')
        print(i)
        
        
        for k in i:
            if k != '_':
                cnt += 1
        
        if cnt == 0:
            result += 1
        
        cnt = 0
        
    return result