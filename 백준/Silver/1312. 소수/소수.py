import sys
read = sys.stdin.readline

A, B, N = map(int, read().rstrip().split())

for i in range(N):
    A = (A % B) * 10
    result = A // B

print(result)