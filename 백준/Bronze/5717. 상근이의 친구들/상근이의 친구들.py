friend_num = []


while True:
    M, F = map(int, input().split())

    
    if M == 0 and F == 0:
        break
    
    friend_num.append(M + F)


for x in friend_num:
    print(x)