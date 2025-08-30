score, diff = map(int, input().split())

if score < diff:
    print(-1)
    exit()

if score == diff == 0:
    print(0, 0)
    exit()

for i in range(1, score):
    a = i
    b = score - i
    if abs(a - b) == diff:
        print(max(a, b), min(a, b))
        exit()

print(-1)