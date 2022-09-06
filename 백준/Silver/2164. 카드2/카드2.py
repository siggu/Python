from collections import deque

N = int(input())

deq = deque(i for i in range(1,N+1))

count = 0

while True:
    if len(deq) <= 1:
        print(deq[0])
        break

    deq.popleft()

    deq.rotate(-1)