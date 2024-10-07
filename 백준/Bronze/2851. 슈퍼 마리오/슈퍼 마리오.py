mushrooms = [int(input()) for _ in range(10)]
num = 0

for mushroom in mushrooms:
    num += mushroom
    if num >= 100:
        if num - 100 > 100 - (num - mushroom):
            num -= mushroom
        
        break

print(num)