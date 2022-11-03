import sys
import heapq
read = sys.stdin.readline

heap = []

N = int(read())

for _ in range(N):
    num = int(read())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap, num)