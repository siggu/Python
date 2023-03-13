from collections import deque

n = int(input())
words = []

for _ in range(n):
    words.append(input())

for i in range(n):
    dq = deque(words[i])
    
    while True:
        dq.append(dq.popleft())
        
        if ''.join(dq) == words[i]:
            break
            
        if ''.join(dq) in words:
            cnt = words.index(''.join(dq))
            words.pop(cnt)
            words.insert(cnt, words[i])

print(len(set(words)))