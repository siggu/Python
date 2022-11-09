import sys
read = sys.stdin.readline

s = read().rstrip()
t = read().rstrip()

for i in range(len(s) + len(t)):
    if s[i % len(s)] != t[i % len(t)]:
        print(0)
        break
else:
    print(1)