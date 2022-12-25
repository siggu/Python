import sys

s = list(map(str, sys.stdin.readline().strip()))

res = ""
word = ""
reverse = True

for c in s:

    if c == '<':
        reverse = False
        res += word
        word = c

    elif c == '>':
        reverse = True
        res += (word + '>')
        word = ""

    elif c == ' ':
        res += word + c
        word = ""

    elif reverse:
        word = c + word

    else:
        word += c

res += word
print(res)