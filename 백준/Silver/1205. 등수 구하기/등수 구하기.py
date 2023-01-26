n, t, p = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    cnt = 0
    if score[n-1] >= t and n == p:
        print(-1)
    else:
        for i in score:
            cnt += 1
            if t >= i:
                print(cnt)
                break
        else:
            print(cnt+1)