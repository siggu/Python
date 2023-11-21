def solution(array, commands):
    answer = []
    
    for i in commands:
        copy_array = array.copy()
        answer.append(sorted(copy_array[i[0]-1:i[1]])[i[-1]-1])
    
    return answer