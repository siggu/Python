from collections import Counter

def solution(want, number, discount):
    answer = 0
    day = dict(zip(want, number))
    
    for i in range(len(discount) - 10 + 1):
        if day == Counter(discount[i:i + 10]):
            answer += 1
    
    return answer