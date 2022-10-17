n = int(input())

for i in range(n):
    word = input().lower()

    if word == word[::-1]:
        print("Yes")
    else:
        print("No")