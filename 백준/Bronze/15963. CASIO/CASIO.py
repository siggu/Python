import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())

if N == M:
    print(1)
else:
    print(0)