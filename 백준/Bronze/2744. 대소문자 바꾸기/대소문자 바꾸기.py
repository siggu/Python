word = input()
result = ""

for i in word:
    if i == i.upper():
        result += i.lower()
    elif i == i.lower():
        result += i.upper()

print(result)