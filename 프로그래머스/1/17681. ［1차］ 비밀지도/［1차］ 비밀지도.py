def solution(n, arr1, arr2): # n: 정사각형 한 변의 길이, arr1: 지도1, arr2: 지도2
    # [1, 2, 4, 8, 16, 32,  ... 2^15] (1 <= n <= 16)
    
    answer = []
    
    for i in range(n):
        word = ""
        if len(bin(arr1[i])[2:]) != n:
            arr1_column = bin(arr1[i])[2:].zfill(n)
        else:
            arr1_column = bin(arr1[i])[2:]
        
        if len(bin(arr2[i])[2:]) != n:
            arr2_column = bin(arr2[i])[2:].zfill(n)
        else:
            arr2_column = bin(arr2[i])[2:]
        
        print(f'arr1_column = {arr1_column}, arr2_column = {arr2_column}')
        
        # print(int(arr1_column[0]) + int(arr2_column[0]))
        
        
        for j in range(n):
            if int(arr1_column[j]) + int(arr2_column[j]) >= 1:
                word += "#"
            elif int(arr1_column[j]) + int(arr2_column[j]) == 0:
                word += " "
        
        answer.append(word)

        
    return answer