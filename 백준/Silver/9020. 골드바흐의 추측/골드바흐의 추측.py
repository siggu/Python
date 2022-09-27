arr = [False, False] + [True]*10002

for i in range(2, 10002):
    if arr[i]:
        for j in range(2*i, 10002, i):
            arr[j] = False

m = int(input())

for i in range(m):
    n = int(input())
    x = n//2
    y = x
    while x>0:
        if arr[x] and arr[y]:
            print(x, y)
            break
        else:
            x-=1
            y+=1