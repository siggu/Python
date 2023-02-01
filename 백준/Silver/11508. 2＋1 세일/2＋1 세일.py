import sys
input = sys.stdin.readline

n = int(input())
price = []

for _ in range(n):
    price.append(int(input()))

price.sort(reverse=True)
arr = []

for i in range(0, len(price), 3):
    arr.append(price[i:i+3])

result = 0

for i in arr:
    if len(i) > 2:
        result += sum(i) - min(i)
    else:
        result += sum(i)

print(result)