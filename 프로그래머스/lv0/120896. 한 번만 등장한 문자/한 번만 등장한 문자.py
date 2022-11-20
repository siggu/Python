def solution(s):
    arr = [0] * 26
    result = ""
    
    for i in s:
        arr[ord(i)-97] += 1
    
    cnt = 0
    for i in arr:
        if i == 1:
            result += chr(cnt+97)
        cnt += 1
        
    return result