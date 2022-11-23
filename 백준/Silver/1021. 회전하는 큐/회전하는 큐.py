import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
num_list = list(map(int, read().rstrip().split()))
dq = deque([i for i in range(1, N+1)])
cnt = 0

for i in num_list:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)