def solution(t, p):
    idx = 0
    answer = 0
    idx_plus = len(p)
    
    for i in range(len(t)):
        if (idx + idx_plus) >= len(t)+1:
            break
        if int(t[idx:idx+idx_plus]) <= int(p):
            answer += 1
            # print(f'int(t[idx:idx+idx_plus]) = {int(t[idx:idx+idx_plus])}, int(p) = {int(p)}')
        idx += 1
    
    return answer