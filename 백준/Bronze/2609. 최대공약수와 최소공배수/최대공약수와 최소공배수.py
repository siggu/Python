import sys
n, m = map(int, sys.stdin.readline().split())

def gcd(x, y):
    while y:
        x ,y = y, x%y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

print(gcd(n, m))
print(lcm(n, m))