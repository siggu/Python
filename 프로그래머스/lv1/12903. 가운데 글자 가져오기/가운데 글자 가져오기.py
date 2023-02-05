def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s)-1)//2: (len(s)-1)//2+2]
    else:
        return s[(len(s)-1)//2]