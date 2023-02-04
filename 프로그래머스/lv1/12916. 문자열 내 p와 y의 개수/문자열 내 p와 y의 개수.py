def solution(s):
    s = s.lower()

    if s.count('p') == s.count('y'):
        return True
    elif s.count('p') != s.count('y'):
        return False
    elif s.count('p') == s.count('y') == 0:
        return True
