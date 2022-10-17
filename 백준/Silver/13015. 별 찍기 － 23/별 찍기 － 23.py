import sys
read = sys.stdin.readline

N = int(read())

print(N * '*' + (2 * N - 3) * ' ' + N * '*')

for i in range(1,N-1):
    print(i * ' ' + 1 * '*' + (N-2) * ' ' + 1 * '*',end='')
    print((2 * N - 3 - (2 * i)) * ' ',end='')
    print(1 * '*' + (N-2) * ' ' + 1 * '*')

print((N-1) * ' ' + 1 * '*' + (N-2) * ' ' + 1 * '*' + (N-2) * ' ' + 1 * '*')

for i in range(N-2, 0, -1):
    print(i * ' ' + 1 * '*' + (N-2) * ' ' + 1 * '*',end='')
    print((2 * N - 3 - (2 * i)) * ' ',end='')
    print(1 * '*' + (N-2) * ' ' + 1 * '*')

print(N * '*' + (2 * N - 3) * ' ' + N * '*')