import sys
read = sys.stdin.readline

N = int(read())
X = list(map(int, read().rstrip().split()))

for i in range(N):
    if X[i] == (int(X[i] ** 0.5) ** 2):
        print(1,end=" ")
    else:
        print(0,end=" ")