def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i):
            if (numbers[i] + numbers[j]) not in answer:
                answer.append(numbers[i] + numbers[j])
            
    return sorted(answer)