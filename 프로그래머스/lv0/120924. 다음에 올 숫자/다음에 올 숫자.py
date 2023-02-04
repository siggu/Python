def solution(common):
    flag = True                         # 등차=True, 등비=False
    num = common[1] - common[0]
    
    if common[1] + num == common[2]:
        return common[-1] + num
    else:
        num = common[1] // common[0]
        return common[-1] * num