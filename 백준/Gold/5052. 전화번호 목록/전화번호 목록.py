import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted([input().rstrip() for _ in range(n)])
    
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print("NO")
            break
    else:
        print("YES")