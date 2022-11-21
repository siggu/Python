import sys
read = sys.stdin.readline

word = list(read().rstrip())
arr = []
tmp = []

for i in range(1, len(word) - 1):
    for j in range(i+1, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        arr.append(first + second + third)

for i in arr:
    tmp.append(''.join(i))

print(sorted(tmp)[0])