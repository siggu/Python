def solution(number):
    length = len(number)
    answer = 0
    
    for i in range(length):
        for j in range(i):
            for z in range(j):
                if number[i] + number[j] + number[z] == 0:
                    answer += 1
    
    return answer