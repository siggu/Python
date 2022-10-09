import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    word = read().rstrip()

    if word == word[::-1]:
        print(0)

    else:
        left_word = list(word)
        right_word = list(word)

        for i in range(int(len(word)/2)):
            if word[i] != word[-(i+1)]:
                left_word.pop(i)
                right_word.pop(-(i+1))
            
                if left_word == left_word[::-1] or right_word == right_word[::-1]:
                    print(1)
                    break
                    
                print(2)
                break