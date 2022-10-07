import sys
read = sys.stdin.readline

N = int(read())

arr = [0, True, False, True, True] + [0] * (N - 4)

if N <= 4:
    pass
else:
    for i in range(5, N+1):
        if False in [arr[i-1], arr[i-3], arr[i-4]]:
            arr[i] = True
        else:
            arr[i] = False

if arr[N]:
    print('SK')
else:
    print('CY')