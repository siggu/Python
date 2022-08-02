S = list(input())
words_list = []
ask = 97

for i in range(26):
    if chr(ask) in S:
        words_list.append(str(S.index(chr(ask))))
    else:
        words_list.append(str(-1))
    ask += 1

print(' '.join(words_list))