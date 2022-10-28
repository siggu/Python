import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    A = list(map(int, read().rstrip().split()))

    A.sort()

    print(A[-3])    