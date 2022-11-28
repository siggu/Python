def solution(spell, dic):
    answer = 0
    cnt = 0
    
    for i in dic:
        for j in spell:
            if len(i) == len(spell):
                if j in i:
                    cnt += 1
        if cnt == len(i):
            return 1
        else:
            cnt = 0
    
    return 2