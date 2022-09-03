N = int(input())
member = []

for x in range(N):
    member.append(list(map(str, input().split())))
    member[x][0] = int(member[x][0])

member.sort(key=lambda x:x[0])

for y in member:
    print(y[0], y[1])