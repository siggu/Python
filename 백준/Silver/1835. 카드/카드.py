from collections import deque

n = int(input())
dq = deque()

dq.appendleft(n)

for i in range(n - 1, 0, -1):
    dq.appendleft(i)

    for j in range(i):
        dq_pop = dq.pop()
        dq.appendleft(dq_pop)

print(*dq)