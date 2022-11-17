def solution(my_string):
    result = []
    
    for i in my_string:
        if i not in 'aeiou':
            result.append(i)
    
    return "".join(result)