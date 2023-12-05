def solution(s):
    word = ""
    stack = []
    result = []
    idx = 0
    
    for i in s:
        word = i
        cnt = 1
        if i in stack:
            for j in s[idx-1::-1]:
                if i == j:
                    result.append(cnt)
                    break
                else:
                    cnt += 1
        else:
            result.append(-1)
        
        idx += 1
        stack.append(i)
    
    return result