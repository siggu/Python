k = 119
arr = [False, False] + [True] * 119

for i in range(2, int(k**0.5)):
    if arr[i]:
        for j in range(i*i, k+1, i):
            arr[j] = False

prime_num = [i for i in range(2, k) if arr[i]]

n = int(input())

for _ in range(n):
    flag = 0
    a = int(input())

    for i in prime_num:
        for j in prime_num:
            if i + j == a:
                flag = 1

    if flag == 1:
        print("Yes")
    else:
        print("No")