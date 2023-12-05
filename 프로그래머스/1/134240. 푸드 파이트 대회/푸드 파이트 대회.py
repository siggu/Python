def solution(food):
    left = ""
    cnt = 1
    
    for i in food[1:]:
        repeat = i // 2
        for j in range(repeat):
            left += str(cnt)
        cnt += 1
    
    return left + "0" + left[::-1]