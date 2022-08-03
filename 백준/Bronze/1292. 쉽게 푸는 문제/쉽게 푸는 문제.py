A, B = map(int, input().split())
count = 1
num_list = []

while True:
    for _ in range(count):
        num_list.append(count)
    count += 1

    if count >= 1000:
        break

print(sum(num_list[A-1:B]))