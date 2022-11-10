def solution(my_string, letter):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == letter:
            my_string[i] = ''
    
    return ''.join(my_string)