import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    k = int(read())
    n = int(read())

    zero_floor = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            zero_floor[j] += zero_floor[j-1]
    print(zero_floor[-1])