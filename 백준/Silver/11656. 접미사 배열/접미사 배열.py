import sys

word = sys.stdin.readline().rstrip()
arr = []

for _ in range(len(word)):
    arr.append(word)

    word = word[1:]

arr.sort()

for x in arr:
    print(x)