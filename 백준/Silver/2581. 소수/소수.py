M = int(input())
N = int(input())
prime_num = []

for x in range(M, N+1):
  count = 0
  for y in range(2, x+1):
    if x % y == 0:
      count += 1
  if count == 1:
    prime_num.append(x)
  else:
    pass

if len(prime_num) >= 1:
  print(sum(prime_num))
  print(min(prime_num))
else:
  print(-1)