import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
num_list = list(map(int, read().rstrip().split()))
prefix_sum = [0]
tmp = 0

for i in num_list:
    tmp += i
    prefix_sum.append(tmp)
    
for i in range(M):
    i, j = map(int, read().rstrip().split())
    
    print(prefix_sum[j] - prefix_sum[i-1])