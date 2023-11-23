def solution(name, yearning, photo):
    result = []
    
    for i in photo:
        yearning_sum = 0
        for j in i:
            for z in name:
                if z == j:
                    yearning_sum += yearning[name.index(z)]
        result.append(yearning_sum)
    
    return result