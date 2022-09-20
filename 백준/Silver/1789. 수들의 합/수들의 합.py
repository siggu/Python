import sys
n = int(sys.stdin.readline().rstrip())

if n == 2:
    print(1)
    exit()
    
result = 0
cnt = 0

for i in range(1, n+1):
    result += i
    cnt += 1
    
    if result == n:
        print(cnt)
        break
    elif result > n:
        print(cnt - 1)
        break