import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    A, B = map(int, read().rstrip().split(','))

    print(A+B)