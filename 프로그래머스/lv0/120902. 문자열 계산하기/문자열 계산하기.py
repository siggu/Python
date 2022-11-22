def solution(my_string):
    my_string = list(map(str, my_string.split(' ')))
    result = 0
    stack = []
    
    for i in my_string:
        if i in "+-":
            stack.append(i)
        else:
            if len(stack) == 0:
                result += int(i)
            else:
                op = stack.pop()
                if op == "+":
                    result += int(i)
                else:
                    result -= int(i)
    
    return result