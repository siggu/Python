def solution(s):
    s = s.split()
    arr = []
    for i in s:
        arr.append(int(i))
        
    return f'{min(arr)} {max(arr)}'