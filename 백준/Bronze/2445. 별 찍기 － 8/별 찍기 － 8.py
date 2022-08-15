N = int(input())

for x in range(1,N+1):
    print(x * '*' + 2*(N - x) * (' ') + x * '*')

for y in range(1, N):
    print((N-y) * '*' + 2 * y * ' ' + (N-y) * '*')