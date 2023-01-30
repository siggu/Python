import sys
import heapq
read = sys.stdin.readline

heap = []
ans = []
N = int(read())

for _ in range(N):
    num = int(read())

    if num == 0:
        if len(heap) == 0:
            ans.append(0)
        else:
            result = heapq.heappop(heap)
            ans.append(result[1])
    else:
        heapq.heappush(heap, (abs(num), num))

for i in ans:
    print(i)