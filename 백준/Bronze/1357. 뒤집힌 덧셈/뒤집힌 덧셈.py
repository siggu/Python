x, y = map(str, input().split())

x = int(x[::-1])
y = int(y[::-1])
result = str(x+y)

print(int(result[::-1]))