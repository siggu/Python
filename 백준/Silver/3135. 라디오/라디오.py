a, b = map(int, input().split())
result = abs(a-b)

for _ in range(int(input())):
    j = int(input())

    if result > abs(j-b):
        result = abs(j-b) + 1

print(result)