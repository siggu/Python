import sys
read = sys.stdin.readline

A, B = map(int, read().rstrip().split())

C = int(read())
C *= 2

if A + B >= C:
    print(A + B - C)
else:
    print(A + B)