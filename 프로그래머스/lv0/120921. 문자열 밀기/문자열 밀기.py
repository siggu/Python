from collections import deque
from copy import deepcopy

def solution(A, B):
    A = deque(A)
    copy_word = deepcopy(A)
    result = 0
    cnt = 0
    arr = []
    
    for i in range(len(A)):
        if ''.join(A) == B:
            arr.append(cnt)
            break
        A.rotate(1)
        cnt += 1
        
    
    for i in range(len(A)):
        if ''.join(copy_word) == B:
            arr.append(cnt)
            break
        copy_word.rotate(-1)
        cnt += 1
    
    if len(arr) == 0:
        return -1
    else:
        return min(arr)