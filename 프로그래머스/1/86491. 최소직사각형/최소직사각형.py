def solution(sizes):
    max_width = []
    max_height = []
    
    for i, j in sizes:
        max_width.append(max(i, j))
        max_height.append(min(i, j))
    
    return max(max_width) * max(max_height)
    