import sys

N, L = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))


for x in range(len(h)):
    minimum = min(h)
    if L >= minimum:
        L += 1
        h.remove(minimum)

print(L)