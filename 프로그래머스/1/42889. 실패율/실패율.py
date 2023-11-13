def solution(N, stages):
    
    result = []
    fail_rate = {}
    stack = []
    answer = []
    
    for i in range(N):
        success = 0
        fail = 0
        
        for j in stages:
            if j > i+1:
                success += 1
            elif j == i+1:
                fail += 1
        try:
            fail_rate[i] = fail / (success + fail)
        except:
            fail_rate[i] = 0
            
    print(f'fail_rate = {fail_rate}')
        
    for i in fail_rate.items():
        stack.append(i[1])
    
    print(f'stack = {stack}')
    
    stack.sort(reverse=True)

    for i in stack:
        for j in fail_rate.items():
            if i == j[1]:
                if (j[0] + 1) in answer:
                    pass
                else:
                    answer.append(j[0] + 1)
    
    return answer