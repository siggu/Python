def solution(dots):
    result = sorted(dots, key = lambda x : (x[0], x[1]))
    
    width = result[-1][0] - result[0][0]
    height = result[-1][1] - result[0][1]
    
    return width * height