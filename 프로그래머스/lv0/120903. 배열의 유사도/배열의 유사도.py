def solution(s1, s2):
    result = 0
    
    for i in s2:
        result += s1.count(i)
    
    return result