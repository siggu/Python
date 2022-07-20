divide_num = []
count = 0

for _ in range(10):
    x = int(input())
    divide_num.append(x % 42)

for x in range(42):
    if x in divide_num:
      count += 1
    
print(count)