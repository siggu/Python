A, B = map(str, input().split())
reverse_A = ''
reverse_B = ''
count = 2

for _ in A:
  reverse_A += A[count]
  reverse_B += B[count]
  count -= 1

reverse_A = int(reverse_A)
reverse_B = int(reverse_B)

if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)