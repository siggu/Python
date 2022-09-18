import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    num = sys.stdin.readline().rstrip()[1:-1].split(",")
    dq = deque(num)
    r = 0
    b = 0

    if n == 0:
        dq = []

    for x in p:
        if x == 'R':
            r += 1
        elif x == 'D':
            if dq:
                if r % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                b = 1
                print('error')
                break
    
    if b == 0:
        if r % 2 == 0:
            print('[' + ','.join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ','.join(dq) + ']')