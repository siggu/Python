T = int(input())

for _ in range(T):
    c, v = map(int, input().split())

    print(f'You get {int(c / v)} piece(s) and your dad gets {int(c % v)} piece(s).')