import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    arr = list(read().rstrip())

    cnt = 0

    for i in arr:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        
        if cnt < 0:
            break
    
    if cnt == 0:
        print('YES')
    else:
        print('NO')