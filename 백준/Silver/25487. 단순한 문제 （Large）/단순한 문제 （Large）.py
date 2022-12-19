import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    a, b, c = map(int, read().rstrip().split())

    print(min(a,b,c))