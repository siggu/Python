def solution(my_string):
    my_string = my_string.lower()
    my_string = sorted(list(my_string))
    
    return "".join(my_string)