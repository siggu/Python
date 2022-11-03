import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    word = list(map(str, read().rstrip().split()))

    for i in word:
        print(i[::-1],end=' ')

    print()