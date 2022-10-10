import sys
read = sys.stdin.readline

N = int(read())
radius = list(map(int, read().rstrip().split()))

def gcd(n, m):
    while n % m != 0:
        n, m = m, n % m
    return m


for i in range(1, N):
    div = gcd(radius[0],radius[i])
    print(f'{int(radius[0] / div)}/{int(radius[i] / div)}')