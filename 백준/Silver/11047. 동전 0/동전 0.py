N, K = map(int, input().split())
count = 0
coin_list = []

for _ in range(N):
    coin_list.append(int(input()))

for x in range(N-1, -1, -1):
  if K == 0:
    break
  elif K >= coin_list[x]:
    count += K // coin_list[x]
    K = K % coin_list[x]

print(count)