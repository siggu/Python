import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())

cnt = 0
cards = list(map(int, read().rstrip().split()))
card_sum = []

while True:
    for i in cards:
        for j in cards[1:]:
            for k in cards[2:]:
                if i == j or j == k or k == i:
                    break
                if i + j + k == M:
                    print(M)
                    cnt = 1
                    exit()
                elif i + j + k >= M:
                    pass
                else:
                    card_sum.append(i + j + k)
    break

if cnt == 0:
    print(max(card_sum))
else:
    pass