def solution(sides):
    max_length = max(sides)
    sides.remove(max_length)
    
    if max_length < sum(sides):
        return 1
    return 2