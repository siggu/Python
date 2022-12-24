n = list(input())
n.sort(reverse=True)
num = ''.join(n)

if num[-1] != '0':
    print(-1)
else:
    if int(num) % 30 == 0:
        print(num)
    else:
        print(-1)