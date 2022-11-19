def d(n):
    num = n
    for i in list(str(n)):
        num += int(i)
    return num

arr = []

for x in range(1, 10001):
    arr.append(d(x))
    if x not in arr:
         print(x)