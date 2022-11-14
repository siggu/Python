from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    
    if direction == "right":
        numbers.rotate(1)
        numbers = list(numbers)
        return numbers
    else:
        numbers.rotate(-1)
        numbers = list(numbers)
        return numbers