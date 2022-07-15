T = int(input())

for i in range(T):
    R,S = map(str, input().split())
    R = int(R)
    S = str(S)
        
    for i in range(len(S)):
        print(R*S[i], end='')
    print()