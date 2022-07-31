import sys
N = int(input())

num_list = [int(sys.stdin.readline()) for _ in range(N)]
num_list.sort()

for x in num_list:
    print(x)