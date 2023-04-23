while True:
    try:
        word = list(input())
        s, d, num, space = 0, 0, 0, 0
        
        for i in range(len(word)):
            if word[i] == " ":
                space += 1
            elif 97 <= ord(word[i]) <= 122:
                s += 1
            elif 65 <= ord(word[i]) <= 90:
                d += 1
            else:
                num += 1
            
        print(s, d, num ,space)
        
    except EOFError:
        break