n = int(input())
good_or_bad = True

for _ in range(3):
    number = list(map(int, input().split()))
    
    if number.count(7) >= 1:
        good_or_bad = True
    else:
        good_or_bad = False

if good_or_bad:
    print(777)
else:
    print(0)