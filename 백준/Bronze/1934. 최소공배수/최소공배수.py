from re import M
import sys
read = sys.stdin.readline

T = int(read())

def gcd(n, m):
    while n % m != 0:
        n, m = m, n % m
    return m

for _ in range(T):
    A, B = list(map(int, read().rstrip().split()))

    print(int(A * B / gcd(A, B)))