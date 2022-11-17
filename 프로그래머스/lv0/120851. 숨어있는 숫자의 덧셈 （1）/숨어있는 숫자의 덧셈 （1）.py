def solution(my_string):
    result = []
    
    for i in my_string:
        if i in '123456789':
            result.append(int(i))
    
    return sum(result)