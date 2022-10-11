def gcd(n, m):
    while n % m != 0:
        n, m = m, n % m
    return m

A, B = map(int, input().split())
print('1' * gcd(A, B))