def solution(score):
    arr = []
    average = []
    
    for i in score:
        average.append(sum(i)/2)
    
    reverse_average = sorted(average, reverse=True)
    
    for i in average:
        arr.append(reverse_average.index(i) + 1)
    
    return arr