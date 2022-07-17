word = input()
word_list = []
compare_list = []
count = len(word_list)


for x in word:
    word_list.append(x)

for y in word_list:
    compare_list.append(word_list[count - 1])
    count -= 1

if word_list == compare_list:
  print(1)
else:
  print(0)