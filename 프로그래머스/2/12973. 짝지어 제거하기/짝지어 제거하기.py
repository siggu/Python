def solution(s):
    stack = []
    
    for i in s:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                for j in range(2):
                    stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0