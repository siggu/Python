import sys
read = sys.stdin.readline

S = read()

for i in S:
    if ord(i) >= 65 and ord(i) <= 90:
        i = ord(i) + 13
        if i > 90:
            i -= 26
        i = chr(i)
        print(i,end='')
    elif ord(i) >= 97 and ord(i) <= 122:
        i = ord(i) + 13
        if i > 122:
            i -= 26
        i = chr(i)
        print(i,end='')
    else:
        print(i,end='')    