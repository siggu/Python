import sys
import math
read = sys.stdin.readline

A, B = map(int, read().rstrip().split())
arr = [True] * (int(math.sqrt(B))+1)
arr[1] = False

for i in range(2, int(math.sqrt(B))+1):
    if arr[i]:
        for j in range(i*i, int(math.sqrt(B))+1, i):
            arr[j] = False

cnt = 0
for i in range(1, len(arr)):
    if arr[i]:
        j = i*i
        while j <= B:
            if j < A:
                j *= i
                continue
            j *= i
            cnt += 1

print(cnt)