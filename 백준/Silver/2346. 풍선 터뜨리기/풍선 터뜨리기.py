from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split())))
result = []

while balloons:
    idx, num = balloons.popleft()
    result.append(idx + 1)

    if num > 0:
        balloons.rotate(-(num - 1))
    else:
        balloons.rotate(-num)

print(*result)