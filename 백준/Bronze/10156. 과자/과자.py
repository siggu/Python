K, N, M = map(int, input().split())

money = (K * N) - M

if money >= 0:
    print(money)
else:
    print(0)
        