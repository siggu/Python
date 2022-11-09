def solution(my_string, n):
    new_string = ''
    
    for i in my_string:
        new_string += n * i
        
    return new_string