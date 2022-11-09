import sys
read = sys.stdin.readline

k = 10**7
arr = [False, False] + [True] * (k+1)

for i in range(2, int(k**0.5)+1):
    if arr[i]:
        for j in range(i+i, k, i):
            arr[j] = False

prime_list = [i for i in range(2, k) if arr[i]]

K = int(read())
print(prime_list[K-1])