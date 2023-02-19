n = int(input())

for i in range(n):
    a = int(input())
    
    for i in range(2, a+1):
        cnt = 0
        if a % i == 0:
            while a % i == 0:
                a = a // i
                cnt += 1
            print(f'{i} {cnt}')
        elif a == 1:
            break