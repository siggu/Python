a = int(input())
b = input()
count = 2

for _ in range(3):
    print(a * int(b[count]))
    count -= 1

print(a * int(b))