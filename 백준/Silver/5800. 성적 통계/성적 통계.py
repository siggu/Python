import sys
read = sys.stdin.readline

K = int(read())

for i in range(1, K+1):
    N = list(map(int, read().rstrip().split()))
    del N[0]

    print(f'Class {i}')

    N.sort(reverse=True)
    gap = N[0] - N[1]

    for j in range(2, len(N)):
        gap = max(gap, N[j-1] - N[j])

    print(f'Max {max(N)}, Min {min(N)}, Largest gap {gap}')