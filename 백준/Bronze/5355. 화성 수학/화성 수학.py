T = int(input())

for _ in range(T):
  result = 0
  test = list(map(str, input().split()))

  test[0] = float(test[0])
  result += test[0]

  for x in test[1:]:
    if x == '@':
      result = result * 3
    elif x == '%':
      result = result + 5
    else:
      result = result - 7

  print(f'{result:.2f}')