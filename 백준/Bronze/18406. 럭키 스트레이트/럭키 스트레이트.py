n = input()
first = n[:len(n)//2]
second = n[len(n)//2:]

result1 = 0
result2 = 0

for i in first:
    result1 += int(i)

for i in second:
    result2 += int(i)

if result1 == result2:
    print("LUCKY")
else:
    print("READY")