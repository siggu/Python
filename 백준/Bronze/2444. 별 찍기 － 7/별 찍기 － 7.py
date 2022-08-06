N = int(input())

for x in range(N-1):
    print(' ' * (N-x-1) + '*' * (x+1),end='')
    print('*' * (x))

for x in range(N):
    print(' ' * x + '*' * (N-x),end='')
    print('*' * (N-x-1))