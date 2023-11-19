def solution(s, n):
    # 소문자: 97~123
    # 대문자: 65~91
    
    result = ""
    
    for i in s:
        if ord(i) == 32:
            result += " "
        elif ord(i) >= 97 and ord(i) <= 122:
            result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
                

    
    return result