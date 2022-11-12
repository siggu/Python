def solution(emergency):
    answer = [0] * len(emergency)
    
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] <= emergency[j]:
                answer[i] += 1
    
    return answer