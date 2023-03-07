import sys
input = sys.stdin.readline
n = int(input())
file = {}

for _ in range(n):
    extension = input().rstrip().split('.')[1]

    if extension not in file:
        file[extension] = 1
    else:
        file[extension] += 1

file = sorted(file.items())

for i in file:
    print(i[0], i[1])