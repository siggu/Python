S = input()
T = input()
count = 0

while (T != S):
    if len(T) == 0:
        count = 1
        print(0)
        break
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
    else:
        count = 1
        print(0)
        break

if count == 0:
    print(1)