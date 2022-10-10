import sys
read = sys.stdin.readline

n = int(read())

def gcd(n, m):
    while n % m != 0:
        n, m = m, n % m
    return m

for _ in range(n):
    a, b = map(int, read().rstrip().split())

    print(int(a * b // gcd(a, b)))