import sys
N = int(sys.stdin.readline())

arr = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

for x in arr:
    print(x,end=' ')