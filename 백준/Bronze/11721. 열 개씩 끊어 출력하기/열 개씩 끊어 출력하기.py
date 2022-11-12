import sys
read = sys.stdin.readline

word = read().rstrip()
cnt = 0

while word:
    print(word[cnt],end='')
    cnt += 1
    if cnt == len(word):
        break
    if cnt % 10 == 0:
        print()