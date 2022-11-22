def solution(quiz):
    cal = []
    result = []
    
    for i in quiz:
        cal.append(i.split("="))
        
    for i in range(len(cal)):
        if eval(cal[i][0]) == eval(cal[i][1]):
            result.append("O")
        else:
            result.append("X")
    
    return result