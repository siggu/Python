T = int(input())
bridge_case = []

for _ in range(T):
  count = 1
  N, M = map(int, input().split())

  for x in range(N):
    count = count * (M - x)
  for y in range(1, N + 1):
    count = count // y
  bridge_case.append(count)

for z in range(T):
  print(bridge_case[z])