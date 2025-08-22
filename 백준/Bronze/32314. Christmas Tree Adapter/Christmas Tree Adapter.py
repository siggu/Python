a = int(input())
w, v = map(int, input().split())
# watt = ampere * volt, ampere = watt / volt

if (w / v) >= a:
    print(1)
else:
    print(0)