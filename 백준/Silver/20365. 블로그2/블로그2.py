n = int(input())
word = list(i for i in input())
first = word[0]

for i in word:
    if first[-1] != i:
        first += i

cnt = first.count("B")

print(min(cnt+1, len(first) - cnt+1))