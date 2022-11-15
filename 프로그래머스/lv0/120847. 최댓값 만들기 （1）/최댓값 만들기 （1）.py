def solution(numbers):
    result = 1
    for i in range(len(numbers)):
        if numbers[i] == max(numbers):
            result *= max(numbers)
            numbers.remove(max(numbers))
            break
            
    result *= max(numbers)
    return result