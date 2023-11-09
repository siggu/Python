def solution(d, budget):
    d.sort()
    answer = 0
    limit = 0
    print(d)
    for i in d:
        print(f'limit: {limit}, answer: {answer}')
        if limit >= budget:
            break
        limit += i
        answer += 1
    
    if limit > budget:
        return answer - 1
    else:
        return answer