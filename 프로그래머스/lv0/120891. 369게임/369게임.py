def solution(order):
    order = str(order)
    
    result = 0
    result += order.count('3')
    result += order.count('6')
    result += order.count('9')
    
    return result