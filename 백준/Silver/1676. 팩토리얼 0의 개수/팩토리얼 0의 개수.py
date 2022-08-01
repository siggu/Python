N = int(input())
factorial = 1
count = 1
zero_count = 0

for x in range(1, N+1):
    factorial *= x

factorial = str(factorial)

for _ in factorial:
    x = factorial[-count]
    if x == '0':
        zero_count += 1
        pass
    else:
        break
    count += 1

print(zero_count)