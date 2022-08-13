while True:
    count = 0
    sentence = input().lower()
    vowel = ['a', 'e', 'i', 'o', 'u']

    if sentence == '#':
        break

    for x in vowel:
        for y in sentence:
            if x == y:
                count += 1
            else:
                pass

    print(count)