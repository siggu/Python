word = input()

for i in "UCPC":
    if i in word:
        word = word[word.index(i) + 1:]
    else:
        print("I hate UCPC")
        exit()
print("I love UCPC")