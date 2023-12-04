def solution(n):
    array = [0, 1]
    
    for i in range(0, n-1):
        array.append(sum(array[i:i+2]) % 1234567)
    
    return array[-1] % 1234657