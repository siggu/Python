import sys
read = sys.stdin.readline

word = read().rstrip()
alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpabet:
    word = word.replace(i,'a')

print(len(word))