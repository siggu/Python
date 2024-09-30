H, W = map(int, input().split())
clouds = [input() for _ in range(H)]
answer = [[0] * W for _ in range(H)]

for i in range(H):
    cnt = 1
    is_cloud = False
    for j in range(W):
        if not is_cloud and clouds[i][j] == '.':
            answer[i][j] = -1
        elif clouds[i][j] == 'c':
            is_cloud = True
            answer[i][j] = 0
            cnt = 1
        elif is_cloud and clouds[i][j] == '.':
            answer[i][j] = cnt
            cnt += 1

for i in answer:
    print(*i, end=' ')
    print()