def solution(n):
    a = n
    
    while True:
        a += 1
        if bin(n)[2:].count("1") == bin(a)[2:].count("1"):
            return a
    