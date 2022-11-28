def solution(a, b):
    cal = a / b
    
    if len(str(cal)) >= 14:
        return 2
    else:
        return 1