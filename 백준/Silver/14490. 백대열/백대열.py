import sys
read = sys.stdin.readline

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

n, m = map(int, read().rstrip().split(':'))

print(f'{int(n/gcd(n, m))}:{int(m/gcd(n, m))}')