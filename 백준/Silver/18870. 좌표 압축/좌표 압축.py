import sys
read = sys.stdin.readline

N = int(read())

arr = list(map(int, read().rstrip().split()))
new_arr = list(set(arr))
new_arr.sort()
idx_dic = {}

for i in range(len(new_arr)):
    idx_dic[new_arr[i]] = i

for j in arr:
    print(idx_dic[j], end=" ")