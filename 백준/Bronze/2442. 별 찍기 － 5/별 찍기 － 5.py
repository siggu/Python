N = int(input())

for x in range(N):
    print(' ' * (N-x-1) + '*' * (x+1),end='')
    print('*' * x)