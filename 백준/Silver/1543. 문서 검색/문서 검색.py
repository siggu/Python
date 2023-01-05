doc = input()
word = input()
cnt = 0
idx = 0

while idx <= len(doc) - len(word):    
    if doc[idx:idx + len(word)] == word:
        cnt += 1
        idx += len(word)
    else:
        idx +=1
    
print(cnt)