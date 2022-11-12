def solution(age):
    age = str(age)
    result = ''
    
    for i in age:
        result += chr(int(i)+97)
    
    return result