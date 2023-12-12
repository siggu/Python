def solution(n):
    arr = [True] * (n+1)
    
    k = int(n ** 0.5)
    
    for i in range(2, k+1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False
    
    return arr[2:].count(True)