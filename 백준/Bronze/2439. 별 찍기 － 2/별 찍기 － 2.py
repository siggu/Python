N = int(input())
count = 1

for x in range(1, N+1):
    if N == count:
      print('*' * count)
    else:
      print(' ' * (N-count-1), '*' * (count))
    count += 1