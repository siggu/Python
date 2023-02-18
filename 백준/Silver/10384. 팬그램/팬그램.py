alphabet = list(range(97, 123))

for t in range(1, int(input())+1) :
    pangram = input().lower()
    check = [0] * 26
    for i in pangram :
        if ord(i) in alphabet :
            check[ord(i)-97] += 1

    if min(check) == 0 :
        print("Case {}: Not a pangram".format(t))
    elif min(check) == 1 :
        print("Case {}: Pangram!".format(t))
    elif min(check) == 2 :
        print("Case {}: Double pangram!!".format(t))
    elif min(check) == 3 :
        print("Case {}: Triple pangram!!!".format(t))