def solution(array):
    arr = [0] * (max(array)+1)
    
    for i in array:
        arr[i] += 1

    cnt = 0
    
    for j in arr:
        if j == max(arr):
            cnt += 1
    
    if cnt > 1:
        return -1
    else:
        return arr.index(max(arr))