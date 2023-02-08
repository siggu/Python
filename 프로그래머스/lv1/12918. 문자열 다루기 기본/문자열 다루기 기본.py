def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            return s.isdigit()
        except:
            return False
        
    return False