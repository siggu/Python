A, B = list(map(str, input().split()))
count = 0

while True:
  if int(B) < int(A):
    print(-1)
    break
    
  if B == A:
    print(count+1)
    break

  if B[len(B)-1] == '1':
    B = B[0:len(B)-1]
    count += 1
  elif int(B[len(B)-1]) % 2 == 0:
    B = str(int(int(B)/2))
    count += 1
  else:
    print(-1)
    break