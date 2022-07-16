N = int(input())
aList = []
money = 0

for _ in range(N):
    x, y, z = map(int, input().split())
    
    if x == y and y == z and x == z:
        money = 10000 + (x * 1000)
        aList.append(money)
    elif x == y and x != z and y != z:
        money = 1000 + (x * 100)
        aList.append(money)
    elif y == z and y != x and z != x:
        money = 1000 + (y * 100)
        aList.append(money)
    elif x == z and x != y and z != y:
        money = 1000 + (x * 100)
        aList.append(money)
    else:
        money = max(x, y, z) * 100
        aList.append(money)

print(max(aList))