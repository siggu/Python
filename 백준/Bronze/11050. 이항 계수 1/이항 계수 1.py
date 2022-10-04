import sys
read = sys.stdin.readline

x = 1
y = 1
z = 1

N, K = map(int, read().rstrip().split())
k = N - K

for i in range(1, N+1):
    x *= i

for j in range(1, K+1):
    y *= j

for l in range(1, k+1):
    z *= l

print(int(x / (y * z)))