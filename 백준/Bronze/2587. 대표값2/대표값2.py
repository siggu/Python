avg = 0
median = []

for _ in range(5):
    num = int(input())

    avg += num
    median.append(num)

median.sort()
print(int(avg/5))
print(median[2])