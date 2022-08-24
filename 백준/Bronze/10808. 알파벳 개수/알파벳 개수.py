arr=[]
alphabet = [0]*26
word=input()

for x in range(97,123,1):
    arr.append(x)

for y in word:
    for z in range(26):
        if ord(y) == arr[z]:
            alphabet[z] += 1
        else:
            alphabet[z] += 0
        
for i in alphabet:
    print(i,end=" ")