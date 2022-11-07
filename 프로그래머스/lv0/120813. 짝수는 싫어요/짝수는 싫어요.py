def solution(n):
    arr = []
    for i in range(1, n+1):
        if i % 2 != 0:
            arr.append(i)
    
    return arr