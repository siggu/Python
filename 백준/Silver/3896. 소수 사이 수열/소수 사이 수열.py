k = 1299709
arr = [False, False] + [True] * (k+1)

for i in range(2, k+1):
    if arr[i]:
        for j in range(i*i, k+1, i):
            arr[j] = False

for _ in range(int(input())):
    N = int(input())
    
    if arr[N]:
        print(0)
    else:
        left = N
        right = N
        cnt = 1
        
        while True:
            left -= 1
            if arr[left]:
                break
            cnt += 1
        while True:
            right += 1
            if arr[right]:
                break
            cnt += 1
        
        print(cnt + 1)