def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        word = ""
        arr1_column = bin(arr1[i])[2:].zfill(n)
        arr2_column = bin(arr2[i])[2:].zfill(n)
        
        for j in range(n):
            if int(arr1_column[j]) + int(arr2_column[j]) >= 1:
                word += "#"
            else:
                word += " "
        
        answer.append(word)

    return answer