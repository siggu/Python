def solution(hp):
    general = 5
    soldier = 3
    work = 1
    cnt = 0
    
    while hp != 0:
        if hp >= general:
            hp -= general
        elif hp >= soldier:
            hp -= soldier
        elif hp >= work:
            hp -= work
        cnt += 1
    
    return cnt