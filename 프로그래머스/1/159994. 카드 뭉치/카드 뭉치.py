def solution(cards1, cards2, goal):
    
    for i in goal:
        if cards1 and i == cards1[0]:
            del cards1[0]
        elif cards2 and i == cards2[0]:
            del cards2[0]
        else:
            return "No"
    
    return "Yes"