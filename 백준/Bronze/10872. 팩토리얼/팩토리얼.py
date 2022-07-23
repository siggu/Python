N = int(input())
result = N

while True:
    if N >= 1:
      result = result * (N - 1)
      N -=1
    else:
      print(1)
      break
    if N == 1:
        print(result)
        break