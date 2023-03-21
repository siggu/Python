import sys
input = sys.stdin.readline

n, q = map(int, input().split())

num_list = list(map(int, input().split()))
num_list = sorted(num_list)

for i in range(1, len(num_list)):
    num_list[i] = num_list[i] + num_list[i - 1]

for _ in range(q):
    l, r = map(int, input().split())

    if l == 1:
        print(num_list[r - 1])
    else:
        print(num_list[r-1] - num_list[l-2])