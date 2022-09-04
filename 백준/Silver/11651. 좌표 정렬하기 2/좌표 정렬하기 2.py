N = int(input())
x_y = []

for _ in range(N):
    x_y.append(list(map(int, input().split())))

x_y.sort(key=lambda x : (x[1],x[0]))

for x in x_y:
    print(x[0], x[1])