import sys
input = sys.stdin.readline

N, K = map(int, input().split())
D = [[0]*(K+1) for _ in range(N+1)]
W = []
V = []

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < W[i-1]:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j], D[i-1][j - W[i-1]] + V[i-1])

print(D[N][K])