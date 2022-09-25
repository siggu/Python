import sys
kda = list(map(str, sys.stdin.readline().rstrip().split('/')))

if int(kda[0]) + int(kda[-1]) < int(kda[1]):
    print('hasu')
elif int(kda[1]) == 0:
    print('hasu')
else:
    print('gosu')