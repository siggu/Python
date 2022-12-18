from collections import deque
n = int(input())
size = list(map(int, input().split()))
size.sort(reverse=True)
size = deque(size)
plus_size = 0
point = 0

for i in range(n):
    if len(size) <= 1:
        break
    plus_size = size[0] + size[1]
    point += (size[0] * size[1])

    # print(size, plus_size)
    size.popleft()
    size.popleft()
    size.appendleft(plus_size)
    

print(point)