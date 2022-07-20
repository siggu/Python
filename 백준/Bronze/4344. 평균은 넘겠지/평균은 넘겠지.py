C = int(input())

for _ in range(C):
    avg = 0
    result = 0
    count = 0
    N = list(map(int, input().split()))
    
    score = N[1:]
    
    for x in score:
        avg += x
    
    avg = avg / N[0]

    for y in score:
      if y > avg:
        count += 1

    result = float(count / N[0] * 100)

    print(f'{result:.3f}%')