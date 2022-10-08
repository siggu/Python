import sys
read = sys.stdin.readline

def gcd(n, m):
    while n % m != 0:
        n, m = m, n % m
    return m

A, B = map(int, read().rstrip().split())
a, b = map(int, read().rstrip().split())

N = gcd(A*b + a*B, B*b) 
print((A*b + a*B)//N, B*b//N)