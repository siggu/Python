N = int(input())
rep = 6
count = 0
result = 1

while True:
    result += rep * count
    count += 1
    if result >= N:
        break
            
print(count)