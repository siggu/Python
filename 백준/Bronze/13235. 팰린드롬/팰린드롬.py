import sys
read = sys.stdin.readline

word = read().rstrip()

if word == word[::-1]:
    print('true')
else:
    print('false')