def solution(cipher, code):
    result = ""
    
    cipher = list(cipher)
    
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            result += cipher[i-1]
    
    return result