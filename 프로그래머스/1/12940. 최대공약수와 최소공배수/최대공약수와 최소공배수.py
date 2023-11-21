def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]