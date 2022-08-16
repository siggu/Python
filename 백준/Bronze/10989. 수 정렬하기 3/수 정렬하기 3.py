import sys

list = [0 for _ in range(10001)]

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    list[num] += 1

for i in range(1, 10001):
    count = list[i]
    for _ in range(count):
        print(i)