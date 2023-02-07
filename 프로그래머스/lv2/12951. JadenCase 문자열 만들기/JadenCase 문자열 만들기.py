def solution(s):
    flag = True        # 새로운 문자
    result = ""
    
    for i in s:
        if flag:
            try:
                result += i.upper()
                flag = False
            except:
                break
        else:
            result += i.lower()
        if i == " ":
            flag = True
        
    return result