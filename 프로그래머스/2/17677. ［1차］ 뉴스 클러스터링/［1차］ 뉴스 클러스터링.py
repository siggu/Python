def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    
    plus_set = []
    
    # print(str1, str2)
    
    for i in range(0, len(str1), 1):
        # print(str1[i:i+2])
        # print(str1[i:i+2].isalpha())
        if str1[i:i+2].isalpha():   # 2개 끊었을 때 알파벳인 경우
            if len(str1[i:i+2]) == 2:   # 길이가 2면
                str1_list.append(str1[i:i+2])   # 리스트에 넣음
        
    # print('---------')
        
    for i in range(0, len(str2), 1):
        # print(str2[i:i+2])
        # print(str2[i:i+2].isalpha())
        if str2[i:i+2].isalpha():   # 2개 끊었을 때 알파벳인 경우
            if len(str2[i:i+2]) == 2:   # 길이가 2면
                str2_list.append(str2[i:i+2])   # 리스트에 넣음
    
    # print(str1_list, str2_list)
    
    str1_list_temp = str1_list.copy()
    str1_list_result = str1_list.copy()
    
    for i in str2_list:
        if i not in str1_list_temp:
            str1_list_result.append(i)
        else:
            str1_list_temp.remove(i)
    
    # print(str1_list_result)
    
    for i in str2_list:
        if i in str1_list:
            str1_list.remove(i)
            plus_set.append(i)
    
    # print(plus_set)
    
    if plus_set == str1_list_result:
        return 65536
    else:
        return int(65536*(len(plus_set) / len(str1_list_result)))