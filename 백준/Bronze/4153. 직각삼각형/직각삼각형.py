while True:
  x, y, z = map(int, input().split())
  side_list = []

  side_list.append(x)
  side_list.append(y)
  side_list.append(z)
  largest_side = max(x, y, z)

  side_list.remove(largest_side)

  if x == 0 and y == 0 and z == 0:
    break
  if pow(largest_side,2) == pow(side_list[0], 2) + pow(side_list[1], 2):
    print("right")
  else:
    print("wrong")