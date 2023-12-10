def solution(people, limit):
    left, right = 0, len(people) - 1
    cnt = 0
    people.sort()
    
    while left <= right:
        # print(f'left = {people[left]}, right = {people[right]}')
        if people[left] + people[right] > limit:
            right -= 1
        elif people[left] + people[right] <= limit:
            left += 1
            right -= 1
            
        cnt+=1

    return cnt