def lean(n=[], m=[]):
    return (m[1] - n[1]) / (m[0] - n[0])

def solution(dots):
    if lean(dots[0], dots[1]) == lean(dots[2], dots[3]):
        return 1
    if lean(dots[0], dots[2]) == lean(dots[1], dots[3]):
        return 1
    if lean(dots[0], dots[3]) == lean(dots[1], dots[2]):
        return 1
    
    return 0