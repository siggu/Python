N = int(input())

num = list(map(int, input().split()))

count = 0

for x in num:
    if x == N:
        count += 1

print(count)