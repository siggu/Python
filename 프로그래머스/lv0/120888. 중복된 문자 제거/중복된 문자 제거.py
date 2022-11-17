def solution(my_string):
    result = []
    arr = []

    for i in my_string:
        arr.append(i)
        cnt = 0
        for j in arr:
            if i == j:
                cnt += 1
        
        if cnt <= 1:
            result.append(i)
    
    return "".join(result)