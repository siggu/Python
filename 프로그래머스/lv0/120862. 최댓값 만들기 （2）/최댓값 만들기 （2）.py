def solution(numbers):
    numbers.sort()
    print(numbers)
    
    result = []
    if len(numbers) <= 3:
        result.append(numbers[0] * numbers[1])
        print(result)
        return max(result)
    else:
        result.append(numbers[0] * numbers[1])
        result.append(numbers[-1] * numbers[-2])
        print(result)
        return max(result)