word = input()
n = int(input())
ring = []
cnt = 0

for _ in range(n):
    ring.append(input())

for i in ring:
    i = i + i[:len(word)]
    
    if word in i:
        cnt += 1

print(cnt)