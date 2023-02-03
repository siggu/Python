b, c, d = map(int, input().split())

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

discount = 0
non_discount = 0

for i in burger, side, drink:
    non_discount += sum(i)

for i in range(min(b, c, d)):
    discount += (burger[i] + side[i] + drink[i]) * 0.9

for i in burger, side, drink:
    discount += sum(i[min(b, c, d)::])

print(non_discount)
print(int(discount))