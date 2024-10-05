money = 1000 - int(input())
cnt = 0
exchange = [500, 100, 50, 10, 5, 1]

for i in range(len(exchange)):
    if money // exchange[i] > 0:
        cnt += money // exchange[i]
        money = money % exchange[i]

print(cnt)