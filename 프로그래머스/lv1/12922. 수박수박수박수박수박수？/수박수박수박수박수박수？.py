def solution(n):
    word = "수박"
    result = ""
    
    if n%2 == 0:
        result = word*(n//2)
    else:
        result = word*(n//2) + "수"
    
    return result