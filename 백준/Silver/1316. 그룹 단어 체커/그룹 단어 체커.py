import sys
n = int(sys.stdin.readline())
count = n

for x in range(n):
    word = sys.stdin.readline()
    for y in range(len(word)-1):
        if word[y] == word[y+1]:
            pass
        elif word[y] in word[y+1:]:
            count -= 1
            break

print(count)