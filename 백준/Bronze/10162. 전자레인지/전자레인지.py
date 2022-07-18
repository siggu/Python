T = int(input())
A_count = 0
B_count = 0
C_count = 0
A = 300
B = 60
C = 10

while True:
    if T % 10 != 0:
        print(-1)
        break

    
    if T % A == 0:
        T = T - A
        A_count += 1
    elif T % B == 0:
        T = T - B
        B_count += 1
    else:
        T = T - C
        C_count += 1
    if T == 0:
        break

if T == 0:
  print(A_count, B_count, C_count)