def solution(my_string):
    result = []
    
    for i in my_string:
        if i in '0123456789':
            result.append(int(i))
    
    result.sort()
    return result