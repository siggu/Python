N, M = map(int ,input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]
cnt = 0
now = 1
end = M

for apple in apples:
    if apple < now:
        cnt += (now - apple)
        now = apple
        end = apple + M - 1
    elif apple > end:
        cnt += (apple - end)
        end = apple
        now = end - M + 1

print(cnt)