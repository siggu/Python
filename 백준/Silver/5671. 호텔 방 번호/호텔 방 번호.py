import sys
read = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    cnt = 0

    for i in range(n, m+1):
        if len(set(str(i))) == len(str(i)):
            cnt += 1
    
    print(cnt)