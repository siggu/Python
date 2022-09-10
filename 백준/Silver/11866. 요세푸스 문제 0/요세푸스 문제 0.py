from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N+1)])
arr = []
count = 0
cnt = 0

while dq:
    count += 1
    if K == count:
        arr.append(dq.popleft())
        count = 0
    else:
        dq.append(dq.popleft())

print('<',end='')

for x in arr:
    cnt += 1
    if cnt == len(arr):
        print(f'{x}',end='')
    else:
        print(f'{x}, ',end='')

print('>')