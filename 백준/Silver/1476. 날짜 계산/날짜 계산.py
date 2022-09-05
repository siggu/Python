E, S, M = map(int, input().split())
count = 1

while True:
    if E == 1 and S == 1 and M == 1:
        print(count)
        break

    E -= 1
    S -= 1
    M -= 1

    count += 1

    if E <= 0:
        E = 15
    if S <= 0:
        S = 28
    if M <= 0:
        M = 19