def solution(rsp):
    result = []
    
    for i in str(rsp):
        if i == '2':
            result.append("0")
        elif i == '0':
            result.append("5")
        else:
            result.append("2")
    
    return ''.join(result)