l = int(input())
words = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
r = 31
m = 1234567891
result = 0

for i in range(l):
    result += ((alphabet.index(words[i])+1) * pow(r, i, m)) % m

print(result)