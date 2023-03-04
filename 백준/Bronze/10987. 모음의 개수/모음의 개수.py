word = input()
cnt = 0

for i in 'aeiou':
    if i in word:
        cnt += word.count(i)

print(cnt)