def solution(array, n):
    arr = []
    min_list = []
    cnt = 0
    
    for i in array:
        arr.append(i)

    for i in range(len(array)):
        array[i] -= n
        array[i] = abs(array[i])
        
    min_num = min(array)
    answer = array.index(min(array))
    
    for i in array:
        if i == min_num:
            cnt += 1
            
    if cnt >= 2:
        print(arr)
        print(array)
        for i in range(len(array)):
            if array[i] == min_num:
                min_list.append(arr[i])
        min_list.sort()
        return min_list[0]
    else:
        return arr[answer]