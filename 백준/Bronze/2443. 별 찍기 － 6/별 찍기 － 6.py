N = int(input())

for x in range(N):
    print(' ' * x + '*' * (N-x),end='')
    print('*' * (N-x-1))