def solution(num_list, n):
    answer = []
    
    first = 0
    last = n
    rep = n
    
    for i in range(len(num_list)//n):
        answer.append(num_list[first:last])
        first += rep
        last += rep
    
    return answer