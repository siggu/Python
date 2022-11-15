import sys
import math
read = sys.stdin.readline


A, B, D = map(int, read().rstrip().split())
arr = [False, False] + [True] * (B+1)
cnt = 0

for i in range(2, int(B**0.5)+1):
    if arr[i]:
        for j in range(i*i, B+1, i):
            arr[j] = False
    
prime_list = [i for i in range(A, B+1) if arr[i]]

for k in prime_list:
    if str(D) in str(k):
        cnt += 1

print(cnt)