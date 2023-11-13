def solution(lottos, win_nums):
    """
    max_rank = 1, min_rank = 6
    lottos를 돌면서 win_nums에 맞는 번호가 
    있다면 max_rank 유지, min_rank -= 1
    없으면 max_rank += 1, min_rank 유지
    lottos에 있는 0의 개수만큼 max_rank -= 0의 개수
    """
    answer = []
    max_rank = 1
    min_rank = 7
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min_rank -= 1
        else:
            max_rank += 1
        
    
    max_rank -= lottos.count(0)
    
    print(max_rank, min_rank)
    
    if max_rank == 7:
        answer.append(max_rank - 1)
        answer.append(min_rank - 1)
    elif min_rank== 7:
        answer.append(max_rank)
        answer.append(min_rank - 1)
    else:
        answer.append(max_rank)
        answer.append(min_rank)
    
    return answer
