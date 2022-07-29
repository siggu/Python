N = int(input())
first_card = set(map(int, input().split()))
M = int(input())
second_card = list(map(int, input().split()))

for x in second_card:
  if x in first_card:
    print(1, end =' ')
  else:
    print(0, end=' ')