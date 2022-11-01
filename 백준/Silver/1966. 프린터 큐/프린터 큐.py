import sys
from collections import deque
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N, M = map(int, read().rstrip().split())
    dq = deque(list(map(int, read().rstrip().split())))
    idx_dq = deque([i for i in range(N)])
    cnt = 0
    
    while dq:
        if dq[0] == max(dq):
            cnt += 1
            dq.popleft()
            if idx_dq.popleft() == M:
                print(cnt)
        else:
            dq.rotate(-1)
            idx_dq.rotate(-1)