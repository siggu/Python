n = int(input())
dp = [1, 2]

if n < 3:
    print(n)
else:
    for i in range(n-2):
        dp.append(dp[-1] + dp[-2])
    print(dp[-1]%10007)