burger_list = []
beverage_list = []
for _ in range(3):
    burger = int(input())
    burger_list.append(burger)

for _ in range(2):
    beverage = int(input())
    beverage_list.append(beverage)

print(min(burger_list) + min(beverage_list) - 50)