from collections import Counter

def solution(k, tangerine):
    array = Counter(tangerine)
    result = 0
    cnt = 0
    
    for i in array.most_common():
        # print(i[1])
        result += i[1]
        cnt += 1
        if result >= k:
            return cnt