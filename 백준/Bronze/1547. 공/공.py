num = int(input())
where = 1

for _ in range(num):
    x, y = map(int, input().split())

    if x == where and y != where:
        where = y
    elif x != where and y == where:
        where = x

print(where)