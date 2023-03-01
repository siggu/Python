import re

n = int(input())
word = input()

num = re.findall("\d+", word)
num = list(map(int, num))

print(sum(num))