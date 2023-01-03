a, p = map(int, input().split())
dp = [a]

while True:
    result = 0
    
    for i in str(dp[-1]):
        result += int(i) ** p

    if result in dp:
        break

    dp.append(result)
    
print(dp.index(result))