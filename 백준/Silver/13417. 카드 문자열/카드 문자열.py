from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    card = deque(map(str, input().split()))
    dq = deque(card.popleft())
    
    while card:
        next_card = card.popleft()
        
        if next_card > dq[0]:
            dq.append(next_card)
        else:
            dq.appendleft(next_card)
    
    print(''.join(dq))