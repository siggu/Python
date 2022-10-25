import sys
read = sys.stdin.readline

n = int(read())
cnt = 0
num = 666

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1