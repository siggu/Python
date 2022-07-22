N = int(input())
count = 0
sum = 0

num = map(int, input().split())

for x in num:
  for y in range(2, x+1):
    if x == 1:
      pass
    elif x % y == 0:
      count += 1

  if count == 1:
    sum += 1
    count = 0
  else:
    count = 0

print(sum)