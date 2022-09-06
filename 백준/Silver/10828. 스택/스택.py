import sys
arr = []

N = int(sys.stdin.readline())

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        arr.insert(0, order[1])
    elif order[0] == 'pop':
        if len(arr) <= 0:
            print(-1)
        else:
            print(arr[0])
            arr.pop(0)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if len(arr) <= 0:
            print(1)
        else:
            print(0)
    else:
        if len(arr) <= 0:
            print(-1)
        else:
            print(arr[0])