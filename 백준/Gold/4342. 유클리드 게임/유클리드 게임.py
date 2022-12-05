import sys
read = sys.stdin.readline

def gcd(n, m):
    if n % m == 0:
        return True
    elif n - m < m:
        return False if gcd(m, n-m) else True
    else:
        return True

while True:
    n, m = map(int, input().split())

    if n == 0:
        break
    elif n < m:
        n, m = m, n
    
    if gcd(n, m):
        print("A wins")
    else:
        print("B wins")