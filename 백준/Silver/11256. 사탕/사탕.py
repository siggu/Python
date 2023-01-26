t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    cnt = 0
    candy = []

    for i in range(n):
        width, height = map(int, input().split())
        candy.append(width * height)
    
    candy.sort(reverse=True)

    for k in candy:
        j -= k
        cnt += 1
        if j <= 0:
            print(cnt)
            break