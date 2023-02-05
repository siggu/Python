def solution(s):
    s = sorted(list(s), reverse=True)
    
    return ''.join(s)